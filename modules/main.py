�
    �=g�0  �                   �*  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZ	d dl
mZ d dlmZmZmZmZmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZmZ d d	lmZ d d
lmZ d dlm Z  d dl!m"Z" d dlm#Z#m$Z$ d dl%m&Z&  edeee��      Z'e'jQ                   ejR                  dg�      �      dedefd��       Z*e'jQ                   ejR                  d�      �      d� �       Z+e'jQ                   ejR                  dg�      �      dedefd��       Z* e,d�       y)�    N)�progress_bar)�API_ID�API_HASH�	BOT_TOKEN�WEBHOOK�PORT)�ClientSession)�listen)�getstatusoutput)�web)�Client�filters)�Message)�	FloodWait)�StickerEmojiInvalid)�message)�InlineKeyboardButton�InlineKeyboardMarkup)�Ashu�bot)�api_id�api_hash�	bot_token�start�mc           
   �   �   K  � |j                  t        j                  t        t	        dd��      gt	        dd��      gg�      ��      � d {  ���  y 7 ��w)Nu5   ✜ ᴀsʜᴜᴛᴏsʜ ɢᴏsᴡᴀᴍɪ 𝟸𝟺 ✜zhttps://t.me/AshutoshGoswami24)�urlu+   🦋 𝐅𝐨𝐥𝐥𝐨𝐰 𝐌𝐞 🦋zhttps://t.me/AshuSupport)�reply_markup)�
reply_textr   �
START_TEXTr   r   )r   r   s     �./modules/m2.py�account_loginr"       s[   � �� �
�,�,����)� )�O�Uu���
 &�&S�Ys�t�u��	
� � � � �s   �AA�
A�A�stopc              �   ��   K  � |j                  dd�      � d {  ���  t        j                  t        j                  t        j                  gt        j
                  ���  y 7 �F�w)Nu$   ♦ 𝐒𝐭𝐨𝐩𝐩𝐞𝐭 ♦T)r   �os�execl�sys�
executable�argv)�_r   s     r!   �restart_handlerr+   1   s@   � �� �
�,�,�=�t�
D�D�D��H�H�S�^�^�S�^�^�7�c�h�h�7� E�s   �A!�A�AA!�uploadc              �   �X  K  � |j                  d�      � d {  ��� }| j                  |j                  j                  �      � d {  ��� }|j	                  �       � d {  ��� }|j                  d�      � d {  ���  d|j                  j                  � �}	 t        |d�      5 }|j                  �       }d d d �       j                  d�      }g }|D ]#  }	|j                  |	j                  dd�      �       �% t        j                  |�       |j                  d	t        |�      � d
��      � d {  ���  | j                  |j                  j                  �      � d {  ��� }
|
j                  }|
j                  d�      � d {  ���  |j                  d�      � d {  ���  | j                  |j                  j                  �      � d {  ��� }|j                  }|j                  d�      � d {  ���  |j                  t        j                   �      � d {  ���  | j                  |j                  j                  �      � d {  ��� }|j                  }|j                  d�      � d {  ���  	 |dk(  rd}n*|dk(  rd}n"|dk(  rd}n|dk(  rd}n|dk(  rd}n
|dk(  rd}nd}|j                  t        j$                  �      � d {  ���  | j                  |j                  j                  �      � d {  ��� }|j                  }|j                  d�      � d {  ���  d}|dk(  r|}n|}|j                  t        j&                  �      � d {  ���  | j                  |j                  j                  �      � d {  ��� x}}|j                  }|j                  d�      � d {  ���  |j                  �       � d {  ���  |j                  }|j)                  d�      s|j)                  d�      rt+        d|� d��       d}n|d k(   t        |�      dk(  rd}nt-        |�      }	 t/        |dz
  t        |�      �      D �]�  }	||	   d   j1                  d!d"�      j1                  d#d$�      j1                  d%d&�      j1                  d'd&�      }d|z   }d(|v r�t3        �       4 �d {  ��� }|j5                  |d)d*d+d,d+d-d.d/d0d1d2d3d4d5d6��7�      4 �d {  ��� }|j                  �       � d {  ��� }t7        j8                  d8|�      j;                  d�      }d d d �      �d {  ���  d d d �      �d {  ���  n�d9|v r.t=        j4                  d:|� �d;d<i�7�      j?                  �       d=   }n�d>|v sd?|v sd9|v sd@|v r=dAd<dBdCdDdEdFdGdH�}d=|� ff} t=        j4                  dI|| �J�      }!|!j?                  �       d=   }nAdK|v r|j                  dL�      dM   }"dN|"z   dOz   }n dP|v r|j                  dL�      dM   }"dQ|"z   dRz   }||	   dS   j1                  dTd&�      j1                  dUd&�      j1                  dLd&�      j1                  dVd&�      j1                  dWd&�      j1                  dXd&�      j1                  dYd&�      j1                  dZd&�      j1                  d[d&�      j1                  d\d&�      j1                  d]d&�      jA                  �       }#tC        |�      jE                  d^�      � d_|#d d` � �}$da|v r
db|� dc|� dd�}%n	db|� de|� df�}%dg|v rdh|$� di|� dj|� dk�}&n/da|v rdl|� dm|� dn|$� dk�}&ndo|v rdp|%� dq|� dn|$� dk�}&n	 dp|%� dr|� dn|$� dk�}&	 dttC        |�      jE                  d^�      � du|#� dv|� dw|� dt�	}'dttC        |�      jE                  d^�      � du|#� dx|� dw|� dt�	}(dy|v r�	 tG        j                  ||$�      � d {  ��� })| jI                  |j                  j                  |)|(�z�      � d {  ��� }*|dz  }t        j                  |)�       tK        jL                  d�       �nds|v ru	 dh|$� d{|� dk�}&|&� d|�},t        jR                  |,�       | jI                  |j                  j                  |$� ds�|(�z�      � d {  ��� }*|dz  }t        j                  |$� ds��       n�d}|$� d~|� d|� d��}-|j                  |-�      � d {  ��� }.tG        jT                  ||&|$�      � d {  ��� }/|/}0|.j                  d�      � d {  ���  tG        jV                  | ||'|0||$|.�      � d {  ���  |dz  }tK        jL                  d�       ��� 	 |j                  d��      � d {  ���  y 7 �	�	7 ���7 ���7 ���# 1 sw Y   ��}xY w#  |j                  d�      � d {  ���7   t        j                  |�       Y y xY w7 ��E7 ��7 ���7 ���7 ���7 ���7 ��s7 ��I7 ��'# t"        $ r d}Y �� w xY w7 ���7 ���7 ���7 ��f7 ��<7 ��7 ��7 ��$7 ���7 ���7 ���# 1 �d {  ���7  sw Y   ���xY w7 ���# 1 �d {  ���7  sw Y   ��xY w7 ��e7 ��8# tN        $ rM}+|j                  tC        |+�      �      � d {  ���7   tK        jL                  |+jP                  �       Y d }+~+��d }+~+ww xY w7 ��# tN        $ rM}+|j                  tC        |+�      �      � d {  ���7   tK        jL                  |+jP                  �       Y d }+~+��ud }+~+ww xY w7 ��!7 ��7 ���7 ���# t"        $ r7}+|j                  d�tC        |+�      � d�|$� d�|� ��      � d {  ���7   Y d }+~+���d }+~+ww xY w# t"        $ r%}+|j                  |+�      � d {  ���7   Y d }+~+��d }+~+ww xY w7 ���w)�Nu(   sᴇɴᴅ ᴍᴇ .ᴛxᴛ ғɪʟᴇ  ⏍Tz./downloads/�r�
z://�   uG   ∝ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐟𝐢𝐥𝐞 𝐢𝐧𝐩𝐮𝐭.u8   ɪɴ ᴛxᴛ ғɪʟᴇ ᴛɪᴛʟᴇ ʟɪɴᴋ 🔗** **uo   **

sᴇɴᴅ ғʀᴏᴍ  ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛᴀʟ ɪs 1uz   ∝ 𝐍𝐨𝐰 𝐏𝐥𝐞𝐚𝐬𝐞 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞�144�256x144�240�426x240�360�640x360�480�854x480�720�1280x720�1080�	1920x1080�UNu   ️ ⁪⁬⁮⁮⁮�xmanzhttp://zhttps://zwget 'z' -O 'thumb.jpg'z	thumb.jpg�nozfile/d/zuc?export=download&id=zwww.youtube-nocookie.com/embedzyoutu.bez?modestbranding=1� z/view?usp=sharing�	visioniasz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zen-US,en;q=0.9zno-cachez
keep-alivezhttp://www.visionias.in/�iframe�navigatez
cross-site�1zuMozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36z("Chromium";v="107", "Not=A?Brand";v="24"z?1z	"Android")�AcceptzAccept-LanguagezCache-Control�
Connection�Pragma�RefererzSec-Fetch-DestzSec-Fetch-ModezSec-Fetch-SitezUpgrade-Insecure-Requestsz
User-Agentz	sec-ch-uazsec-ch-ua-mobilezsec-ch-ua-platform)�headersz(https://.*?playlist.m3u8.*?)\"zvideos.classplusappzChttps://api.classplusapp.com/cams/uploader/video/jw-signed-url?url=�x-access-token�\eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9r   ztencdn.classplusappz media-cdn-alisg.classplusapp.comzmedia-cdn.classplusappzapi.classplusapp.comzMobile-Androidz1.4.37.1�18�5d0d17ac8b3c9f51z(2848b866799971ca_2848b8667a33216c_SDK-30�gzip)�HostrJ   z
user-agentzapp-versionzapi-versionz	device-idzdevice-detailszaccept-encodingz>https://api.classplusapp.com/cams/uploader/video/jw-signed-url)rI   �paramsz/utkarshapp.mpd�/�����z$https://apps-s3-prod.utkarshapp.com/z/utkarshapp.comz/master.mpdz&https://d26g5bnklkwsh4.cloudfront.net/z/master.m3u8r   �	�:�+�#�|�@�*�.�https�http�   z) �<   �youtuz
b[height<=z][ext=mp4]/bv[height<=z!][ext=mp4]+ba[ext=m4a]/b[ext=mp4]z]/bv[height<=z]+ba/b/bv+ba�acecwplyzyt-dlp -o "z" -f "bestvideo[height<=zQ]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "�"z yt-dlp -i -f "bestvideo[height<=z=]+bestaudio" --no-keep-video --remux-video mkv --no-warning "z" -o "zplayer.vimeozyt-dlp -f "z/+bestaudio" --no-keep-video --remux-video mkv "z%" --no-keep-video --remux-video mkv "z.pdfz**z. u   .mkv

✉️ Batch Name :  » u   

Downloaded By » u   .pdf

✉️ Batch Name :  » �drive)�chat_id�document�captionz.pdf" "z -R 25 --fragment-retries 25uZ   **❊⟱ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ⟱❊ »

📝 𝐍𝐚𝐦𝐞 » u"   

⌨ 𝐐𝐮𝐥𝐢𝐭𝐲 » u   

🔗 𝐔𝐑𝐋 »** `�`uZ   ⌘ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐮𝐩𝐭𝐞𝐝
u   
⌘ 𝐍𝐚𝐦𝐞 » u   

⌘ 𝐋𝐢𝐧𝐤 » uE   ✅ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐨𝐧𝐞),r   r
   �chat�id�download�delete�open�read�split�appendr%   �remove�edit�len�textr   �Q1_TEXT�	Exception�C1_TEXT�T1_TEXT�
startswithr   �int�range�replacer	   �get�re�search�group�requests�json�strip�str�zfill�helper�send_document�time�sleepr   �x�system�download_video�send_vid)1r   r   �editable�inputr�   �path�f�content�links�i�input0�raw_text�input1�	raw_text0�input2�	raw_text2�res�input3�	raw_text3�highlighter�MR�input6r   �	raw_text6�thumb�count�Vr   �session�resprr   rI   rP   �responserh   �name1�name�ytf�cmd�cc�cc1�ka�copy�e�download_cmd�Show�prog�res_file�filenames1                                                    r!   r"   r"   7   s�  � �� ��\�\�"L�M�M�H��:�:�h�m�m�&6�&6�7�7�E��n�n���A�
�,�,�t�
����!�&�&�)�)��%�D���!�S�\� 	�Q��f�f�h�G�	��-�-��%����� 	,�A��L�L������*�+�	,�
�	�	�!�� �-�-�
B�3�u�:�,�  O@�  	A�� � �  �J�J�x�}�}�'7�'7�8�8�F��{�{�H�
�-�-��
���
�-�-�  U�  V�  V�  V��J�J�x�}�}�'7�'7�8�8�F����I�
�-�-��
���
�-�-����
%�%�%��J�J�x�}�}�'7�'7�8�8�F����I�
�-�-��
��������C��%���C��%���C��%���C��%���C��&� ��C��C� �-�-����
%�%�%��J�J�x�}�}�'7�'7�8�8�F����I�
�-�-��
���'�K��F������
�-�-����
%�%�%� �Z�Z����(8�(8�9�9�9�F�W����I�
�-�-��
���
�/�/�
����K�K�E����	�"�e�&6�&6�z�&B��&���'7�8�9������
�5�z�Q�����H���d��u�q�y�#�e�*�-� `	�A� �a�������$<�=���9�:�F���,�b�1���,�b�1� � �q�.�C��c�!�(�?� � �g�&�{�{�� 'p�/?�-7�*6�&0�'A�.6�.8�.:�9<� +b�)S�04�2=�!�  +�  � � �$ �%)�Y�Y�[�0�� �i�i�(J�D�Q�W�W����)� �� � �2 '�#�-��l�l�Y�Z]�Y^�_�(�  +I���
 �$�&�� �� &��,�5��<�(�C�/�+�s�2� 3� 'E�"2�#-�#'�!3�&P�'-�	�� !�S�E�+�-��#�<�<�T�#�!���
 �m�m�o�e�,��"�c�)��Y�Y�s�^�B�'��<�r�A�DU�U���#�%��Y�Y�s�^�B�'��>��C�n�T�� �a�������r�"����b�!����b�!����b�!����b�!����b�!����b�!����b�!����b�!����"�%�����$���� � �%�j�&�&�q�)�*�"�U�3�B�Z�L�9�D��#�~�"�9�+�-C�I�;�No�p��"�9�+�]�9�+�\�R���S� �#�D�6�)A�)��  M^�  _b�  ^c�  cd�  e���C��8���  DA�  BE�  AF�  FL�  MQ�  LR�  RS�  T���3�&�#�C�5�(W�X[�W\�\b�cg�bh�hi�j���#�C�5�(M�c�U�RX�Y]�X^�^_�`��.��#�e�*�*�*�1�-�.�b�1E�0F�Ff�gp�fq�  rG�  HJ�  GK�  KM�  N���3�u�:�+�+�A�.�/�r�2F�1G�Gg�hq�gr�  sH�  IK�  HL�  LN�  O���c�>�!�#)�?�?�3��#=�=��%(�%6�%6�$%�F�F�I�I��C� &7� &�  �� ��
���	�	�"���
�
�1�� �s�]�!� +�D�6����Q�?��*-��.J�'K���	�	�,�/�%(�%6�%6�$%�F�F�I�I�4�&���s� &7� &�  �� ��
���	�	�T�F�$�-�0� z�z~�y�  @d�  en�  do�  oK�  LO�  KP�  PQ�  R�D�!"���d�!3�3�D�%+�%:�%:�3��T�%J�J�H�'�H��+�+�d�+�+�+� �/�/�#�q�"�h��t�T�R�R�R��Q�J�E��J�J�q�M��u`	�H �,�,�^�
_�_�_�q N��7������
	� 	����l�l�d�e�e�e�
�	�	�!������ 9���� V��8����%��8����  � ����� &��8���� &��9������6����&  1��'�� � � ���� � � ��X >�� �� %� !��l�l�3�q�6�2�2�2��
�
�1�3�3�� ��!�� ��
 %� !��l�l�3�q�6�2�2�2��
�
�1�3�3�� ��!�� 4��J��+��R�� � ��l�l�q�ru�vw�rx�qy�  zT�  UY�  TZ�  Zv�  wz�  v{�  |�� � � ��	�� � ��l�l�1�o������_�s�  �l*�d �,l*�d#�l*�d&�l*�5d)�6l*�d9 � d,�1Ad9 �	!l*�*e/�+,l*�e2�$l*�<e5�=l*�e8�,l*�e;�$l*�'e>�(&l*�f�,l*�;f�<$l*� f�!l*�&2f
 �"l*�:f�;,l*�'f�($l*�f"�2l*�?f%� ,l*�,f(�-&l*�f+�l*�+f.�,A%l*�A;k6 �f1�k6 �'g�8f4
�9g�<f=�f7
�)f=�:g�f:�g�
k6 �g�Hk6 �Aj3�.g2�g,�/g2�7g/�83g2�+j3�2Ai�i�!i�%!j3�j'�j3�%j*�&j3� j-�"j3�#j0�$j3�k6 �l*�l'�l*�#l*�&l*�)l*�,d6�1d9 �9e,�e�e,�*l*�2l*�5l*�8l*�;l*�>l*�l*�l*�l*�
f�l*�f�l*�l*�"l*�%l*�(l*�+l*�.l*�1k6 �4g�7f=�:g�=g�g�g�g�k6 �g)	�g�g)	�$k6 �,g2�/g2�2	i�;i�h�$i�=j3�k6 �i�j3�i�	j$�j�4i7�5$j�j3�k6 �j$�$j3�*j3�-j3�0j3�3	k3�<&k.�"k%�#k.�(k6 �.k3�3k6 �6	l$�?l�l�l�l*�l$�$l*u   3>> DONE✅ [main.py]
)-r%   r|   r'   r�   r�   �asyncior   �
subprocess�corer�   �utilsr   �varsr   r   r   r   r   �aiohttpr	   �pyromodr
   r   r   �pyrogramr   r   �pyrogram.typesr   �pyrogram.errorsr   �*pyrogram.errors.exceptions.bad_request_400r   �!pyrogram.types.messages_and_mediar   r   r   �styler   r   �
on_message�commandr"   r+   �print� �    r!   �<module>r�      s  �� 	� 	� 
� � � � � � � � ;� ;� !� � &� � $� "� %� J� 5� E� � �U�6�H�	�J��
 ��������	�*�+��V� �� � ,��  ��������'�(�8� )�8�
 ��������
�+�,�y`�V� y`�� y`� -�y`�x ��  r�   