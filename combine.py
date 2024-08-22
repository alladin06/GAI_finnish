import streamlit as st
from streamlit_option_menu import option_menu
# from main import main
from notes import notes_main
from enter_data import main_data
from app import nearby_hospi
from visualize_data import  track_progress_main
from acne import main_acne
from sayantan import sos_main
# from login import main_l

def main():

    PAGE_CONFIG = {"page_title": "Geriatrinen tekoäly",
               "page_icon": "icon.png", "layout": "centered"}
    st.set_page_config(**PAGE_CONFIG)
    
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://img.freepik.com/premium-photo/green-background-with-bokeh-rays_582451-37.jpg");
    background-size: cover;
    background-position: ylä vasen;
    background-repeat: ei toistu;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.sidebar.title("Geriatrinen tekoäly")
    menu = ["Kirjaudu sisään", "Terveystietojen tallennus", "Edistyksen seuranta", "Lähellä olevien sairaaloiden etsiminen",  "Hätä-SOS", "Muistiinpanot","Akneen tunnistus","Lähellä olevat tapahtumat"]
    with st.sidebar:
        app_selection = option_menu(
        menu_title = None,
        options = menu,
        # icons = ['talo', 'taulu', 'kortti-tarkistuslista', 'emoji-hymy', 'päiväkirja']
    )
    # app_selection = st.sidebar.radio("Valitse vaihtoehto", ["Tiedot","Lääkemuistutus", "Muistiinpanot", "Lähellä olevien sairaaloiden etsiminen", "Edistyksen seuranta", "Hätä-SOS"])

    if app_selection == "Lääkemuistutus":
        # main()
        pass
    # elif app_selection=="Kirjaudu sisään":
    #     main_l()
        
    elif app_selection == "Muistiinpanot":
        notes_main()
    elif app_selection == "Lähellä olevien sairaaloiden etsiminen":
        nearby_hospi()
        # pass
    elif app_selection == "Edistyksen seuranta":
        track_progress_main()
        # pass
    elif app_selection == "Hätä-SOS":
        sos_main()
        # pass
    elif app_selection=="Terveystietojen tallennus":
        # pass
        main_data()
    elif app_selection=="Akneen tunnistus":
        main_acne()
    elif app_selection == "Lähellä olevat tapahtumat":st.markdown("""
    **Etätapahtuma**: Digivartti: aiheena Google Kalenteri  
    **Milloin:** Pe, 20.9.2024 klo 10-10.30  
    **Missä:** etänä Zoomissa  
    [Lisää tietoa](https://www.entersenior.fi/tapahtumat/digivartti-0924/)

    **Lähitapahtuma**: Ratkaisuja hyvään arkeen  
    **Milloin:** Ke-To, 2-3.10.2024  
    **Missä:** Helsingin messukeskus, Messuaukio 1, 00520 Helsinki  
    [Lisää tietoa](https://hyvaika.expomark.fi/)

    **Matka:** Pohjois-Portugali, Porto ja portviinitilat  
    **Milloin:** Ma-La, 21-26.10.2024  
    **Missä:** Porto, Portugali  
    [Lisää tietoa](https://kilta.senioriliitto.fi/Tapahtumat/tapahtumatiedot.aspx?id=28261)

    **Hybriditapahtuma:** Tunnista nettihuijaus  
    **Milloin:** Ke, 23.10.2024 klo 13.30-15.00  
    **Missä:** etänä Zoomissa, katsomo Kampissa  
    [Lisää tietoa](https://www.entersenior.fi/tapahtumat/tunnista-nettihuijaus/)

    **Lähitapahtuma:** Ohjattu kuntosali  
    **Milloin:** Ma, 30.12.2024 klo 10.00-11.00  
    **Missä:** Myllypuron seniorikeskus/Palvelukeskus, Myllymatkantie 4, Helsinki  
    [Lisää tietoa](https://tapahtumat.hel.fi/fi/events/helsinki:agh3rorroe)
    """)


if __name__ == "__main__":
    main()
