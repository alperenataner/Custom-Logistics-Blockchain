import tkinter as tk
from tkinter import ttk, messagebox
from CustomsLogistics import CustomsLogisticsBlockchain
import uuid
from datetime import datetime
import customtkinter as ctk

class CustomsLogisticsGUI:
    def __init__(self):
        self.chain = CustomsLogisticsBlockchain()
        
        # Ana pencere ayarları
        self.root = ctk.CTk()
        self.root.title("Gümrük ve Lojistik Takip Sistemi")
        self.root.geometry("1200x800")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Ana frame
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Başlık
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Gümrük ve Lojistik Takip Sistemi",
            font=("Helvetica", 24, "bold")
        )
        self.title_label.pack(pady=20)
        
        # Butonlar için frame
        self.button_frame = ctk.CTkFrame(self.main_frame)
        self.button_frame.pack(fill="x", padx=20, pady=10)
        
        # Butonlar
        self.create_buttons()
        
        # İçerik frame
        self.content_frame = ctk.CTkFrame(self.main_frame)
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Başlangıçta boş bir içerik göster
        self.show_welcome()
    
    def create_buttons(self):
        buttons = [
            ("Yeni Gönderi Oluştur", self.show_new_shipment),
            ("Gönderi Sorgula", self.show_shipment_query),
            ("Gönderi Güncelle", self.show_shipment_update),
            ("Tüm Gönderiler", self.show_all_shipments),
            ("Blockchain Görüntüle", self.show_blockchain),
            ("Bütünlük Kontrolü", self.check_integrity)
        ]
        
        for text, command in buttons:
            btn = ctk.CTkButton(
                self.button_frame,
                text=text,
                command=command,
                width=200,
                height=40
            )
            btn.pack(side="left", padx=10, pady=5)
    
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_welcome(self):
        self.clear_content()
        welcome_text = """
        Gümrük ve Lojistik Takip Sistemine Hoş Geldiniz!
        
        Bu sistem, gönderilerinizi blockchain teknolojisi ile güvenli bir şekilde takip etmenizi sağlar.
        
        Lütfen yapmak istediğiniz işlemi seçiniz.
        """
        welcome_label = ctk.CTkLabel(
            self.content_frame,
            text=welcome_text,
            font=("Helvetica", 14),
            justify="center"
        )
        welcome_label.pack(pady=50)
    
    def show_new_shipment(self):
        self.clear_content()
        
        # Form frame
        form_frame = ctk.CTkFrame(self.content_frame)
        form_frame.pack(padx=20, pady=20)
        
        # Takip numarası
        tracking_number = str(uuid.uuid4())[:8].upper()
        tracking_label = ctk.CTkLabel(
            form_frame,
            text=f"Takip Numarası: {tracking_number}",
            font=("Helvetica", 14, "bold")
        )
        tracking_label.pack(pady=10)
        
        # Form alanları
        fields = ["Gönderici Adı", "Alıcı Adı", "Gönderi Açıklaması", "Gönderi Değeri (TL)"]
        entries = {}
        
        for field in fields:
            frame = ctk.CTkFrame(form_frame)
            frame.pack(fill="x", padx=20, pady=5)
            
            label = ctk.CTkLabel(frame, text=field, width=150)
            label.pack(side="left", padx=5)
            
            entry = ctk.CTkEntry(frame, width=300)
            entry.pack(side="left", padx=5)
            entries[field] = entry
        
        def submit():
            # Form verilerini al
            data = {field: entry.get() for field, entry in entries.items()}
            
            # Boş alan kontrolü
            if any(not value for value in data.values()):
                messagebox.showerror("Hata", "Lütfen tüm alanları doldurunuz!")
                return
            
            # Transaction oluştur
            transaction = {
                "tracking_number": tracking_number,
                "sender": data["Gönderici Adı"],
                "receiver": data["Alıcı Adı"],
                "description": data["Gönderi Açıklaması"],
                "value": data["Gönderi Değeri (TL)"],
                "status": "Gönderi Oluşturuldu",
                "customs_status": "Gümrük İşlemi Bekliyor",
                "location": "Gönderici Depo"
            }
            
            # Blockchain'e ekle
            self.chain.add_transaction(transaction)
            self.chain.mine_pending_transaction()
            
            messagebox.showinfo("Başarılı", "Gönderi başarıyla oluşturuldu!")
            self.show_welcome()
        
        # Gönder butonu
        submit_btn = ctk.CTkButton(
            form_frame,
            text="Gönderi Oluştur",
            command=submit,
            width=200
        )
        submit_btn.pack(pady=20)
    
    def show_shipment_query(self):
        self.clear_content()
        
        query_frame = ctk.CTkFrame(self.content_frame)
        query_frame.pack(padx=20, pady=20)
        
        # Takip numarası girişi
        input_frame = ctk.CTkFrame(query_frame)
        input_frame.pack(fill="x", padx=20, pady=10)
        
        label = ctk.CTkLabel(input_frame, text="Takip Numarası:", width=150)
        label.pack(side="left", padx=5)
        
        entry = ctk.CTkEntry(input_frame, width=300)
        entry.pack(side="left", padx=5)
        
        # Sonuç frame
        result_frame = ctk.CTkFrame(query_frame)
        result_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        def search():
            tracking_number = entry.get().strip()
            if not tracking_number:
                messagebox.showerror("Hata", "Lütfen bir takip numarası giriniz!")
                return
            
            shipment = self.chain.get_shipment_status(tracking_number)
            
            # Önceki sonuçları temizle
            for widget in result_frame.winfo_children():
                widget.destroy()
            
            if shipment:
                # Sonuçları göster
                for key, value in shipment.items():
                    frame = ctk.CTkFrame(result_frame)
                    frame.pack(fill="x", padx=10, pady=5)
                    
                    key_label = ctk.CTkLabel(frame, text=f"{key}:", width=150)
                    key_label.pack(side="left", padx=5)
                    
                    value_label = ctk.CTkLabel(frame, text=str(value))
                    value_label.pack(side="left", padx=5)
            else:
                label = ctk.CTkLabel(result_frame, text="Gönderi bulunamadı!")
                label.pack(pady=20)
        
        # Arama butonu
        search_btn = ctk.CTkButton(
            input_frame,
            text="Sorgula",
            command=search,
            width=100
        )
        search_btn.pack(side="left", padx=10)
    
    def show_shipment_update(self):
        self.clear_content()
        
        update_frame = ctk.CTkFrame(self.content_frame)
        update_frame.pack(padx=20, pady=20)
        
        # Takip numarası girişi
        input_frame = ctk.CTkFrame(update_frame)
        input_frame.pack(fill="x", padx=20, pady=10)
        
        label = ctk.CTkLabel(input_frame, text="Takip Numarası:", width=150)
        label.pack(side="left", padx=5)
        
        entry = ctk.CTkEntry(input_frame, width=300)
        entry.pack(side="left", padx=5)
        
        # Durum seçimi frame
        status_frame = ctk.CTkFrame(update_frame)
        status_frame.pack(fill="x", padx=20, pady=10)
        
        status_var = tk.StringVar()
        statuses = [
            "Gümrük İşlemlerinde",
            "Gümrük İşlemi Tamamlandı",
            "Yolda",
            "Teslim Edildi"
        ]
        
        def search():
            tracking_number = entry.get().strip()
            if not tracking_number:
                messagebox.showerror("Hata", "Lütfen bir takip numarası giriniz!")
                return
            
            shipment = self.chain.get_shipment_status(tracking_number)
            
            # Önceki sonuçları temizle
            for widget in status_frame.winfo_children():
                widget.destroy()
            
            if shipment:
                # Mevcut durumu göster
                current_status = ctk.CTkLabel(
                    status_frame,
                    text=f"Mevcut Durum: {shipment['status']}",
                    font=("Helvetica", 12, "bold")
                )
                current_status.pack(pady=10)
                
                # Durum seçenekleri
                for status in statuses:
                    radio = ctk.CTkRadioButton(
                        status_frame,
                        text=status,
                        variable=status_var,
                        value=status
                    )
                    radio.pack(pady=5)
                
                def update():
                    new_status = status_var.get()
                    if not new_status:
                        messagebox.showerror("Hata", "Lütfen yeni bir durum seçiniz!")
                        return
                    
                    shipment["status"] = new_status
                    self.chain.add_transaction(shipment)
                    self.chain.mine_pending_transaction()
                    
                    messagebox.showinfo("Başarılı", "Gönderi durumu güncellendi!")
                    self.show_welcome()
                
                # Güncelle butonu
                update_btn = ctk.CTkButton(
                    status_frame,
                    text="Durumu Güncelle",
                    command=update,
                    width=200
                )
                update_btn.pack(pady=20)
            else:
                label = ctk.CTkLabel(status_frame, text="Gönderi bulunamadı!")
                label.pack(pady=20)
        
        # Arama butonu
        search_btn = ctk.CTkButton(
            input_frame,
            text="Sorgula",
            command=search,
            width=100
        )
        search_btn.pack(side="left", padx=10)
    
    def show_all_shipments(self):
        self.clear_content()
        
        shipments = self.chain.get_all_shipments()
        
        if not shipments:
            label = ctk.CTkLabel(
                self.content_frame,
                text="Henüz gönderi bulunmuyor.",
                font=("Helvetica", 14)
            )
            label.pack(pady=50)
            return
        
        # Scrollable frame
        scroll_frame = ctk.CTkScrollableFrame(self.content_frame)
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        for tracking_number, shipment in shipments.items():
            shipment_frame = ctk.CTkFrame(scroll_frame)
            shipment_frame.pack(fill="x", padx=10, pady=5)
            
            # Takip numarası
            tracking_label = ctk.CTkLabel(
                shipment_frame,
                text=f"Takip No: {tracking_number}",
                font=("Helvetica", 12, "bold")
            )
            tracking_label.pack(anchor="w", padx=10, pady=5)
            
            # Diğer bilgiler
            info_frame = ctk.CTkFrame(shipment_frame)
            info_frame.pack(fill="x", padx=20, pady=5)
            
            for key, value in shipment.items():
                if key != "tracking_number":
                    frame = ctk.CTkFrame(info_frame)
                    frame.pack(fill="x", padx=5, pady=2)
                    
                    key_label = ctk.CTkLabel(frame, text=f"{key}:", width=150)
                    key_label.pack(side="left", padx=5)
                    
                    value_label = ctk.CTkLabel(frame, text=str(value))
                    value_label.pack(side="left", padx=5)
    
    def show_blockchain(self):
        self.clear_content()
        
        # Scrollable frame
        scroll_frame = ctk.CTkScrollableFrame(self.content_frame)
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        for block in self.chain.chain:
            block_frame = ctk.CTkFrame(scroll_frame)
            block_frame.pack(fill="x", padx=10, pady=10)
            
            # Block başlığı
            header_frame = ctk.CTkFrame(block_frame)
            header_frame.pack(fill="x", padx=10, pady=5)
            
            index_label = ctk.CTkLabel(
                header_frame,
                text=f"Block #{block.index}",
                font=("Helvetica", 14, "bold")
            )
            index_label.pack(side="left", padx=10)
            
            time_label = ctk.CTkLabel(
                header_frame,
                text=datetime.fromtimestamp(block.timestamp).strftime('%Y-%m-%d %H:%M:%S')
            )
            time_label.pack(side="right", padx=10)
            
            # Block detayları
            details_frame = ctk.CTkFrame(block_frame)
            details_frame.pack(fill="x", padx=20, pady=5)
            
            hash_frame = ctk.CTkFrame(details_frame)
            hash_frame.pack(fill="x", padx=5, pady=2)
            
            prev_hash_label = ctk.CTkLabel(hash_frame, text="Önceki Hash:", width=150)
            prev_hash_label.pack(side="left", padx=5)
            
            prev_hash_value = ctk.CTkLabel(hash_frame, text=block.previous_hash)
            prev_hash_value.pack(side="left", padx=5)
            
            curr_hash_frame = ctk.CTkFrame(details_frame)
            curr_hash_frame.pack(fill="x", padx=5, pady=2)
            
            curr_hash_label = ctk.CTkLabel(curr_hash_frame, text="Bu Block Hash:", width=150)
            curr_hash_label.pack(side="left", padx=5)
            
            curr_hash_value = ctk.CTkLabel(curr_hash_frame, text=block.hash)
            curr_hash_value.pack(side="left", padx=5)
            
            # İşlemler
            if block.transactions:
                transactions_frame = ctk.CTkFrame(details_frame)
                transactions_frame.pack(fill="x", padx=5, pady=5)
                
                trans_label = ctk.CTkLabel(
                    transactions_frame,
                    text="İşlemler:",
                    font=("Helvetica", 12, "bold")
                )
                trans_label.pack(anchor="w", padx=5, pady=5)
                
                for transaction in block.transactions:
                    trans_frame = ctk.CTkFrame(transactions_frame)
                    trans_frame.pack(fill="x", padx=20, pady=2)
                    
                    for key, value in transaction.items():
                        item_frame = ctk.CTkFrame(trans_frame)
                        item_frame.pack(fill="x", padx=5, pady=1)
                        
                        key_label = ctk.CTkLabel(item_frame, text=f"{key}:", width=150)
                        key_label.pack(side="left", padx=5)
                        
                        value_label = ctk.CTkLabel(item_frame, text=str(value))
                        value_label.pack(side="left", padx=5)
    
    def check_integrity(self):
        if self.chain.is_chain_valid():
            messagebox.showinfo("Bütünlük Kontrolü", "Blockchain güvende ve bütünlüğü korunuyor.")
        else:
            messagebox.showerror("Bütünlük Kontrolü", "Blockchain'de bir sorun tespit edildi!")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CustomsLogisticsGUI()
    app.run() 