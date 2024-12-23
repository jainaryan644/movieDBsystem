PGDMP  !    .                |            mdb_412    17.2    17.2 4               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false                       1262    16388    mdb_412    DATABASE     �   CREATE DATABASE mdb_412 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE mdb_412;
                     postgres    false            �            1259    16523    cast_    TABLE     d   CREATE TABLE public.cast_ (
    pid integer NOT NULL,
    mid integer NOT NULL,
    roles text[]
);
    DROP TABLE public.cast_;
       public         heap r       postgres    false            �            1259    16530    crew_    TABLE     R   CREATE TABLE public.crew_ (
    pid integer NOT NULL,
    mid integer NOT NULL
);
    DROP TABLE public.crew_;
       public         heap r       postgres    false            �            1259    16535 	   director_    TABLE     V   CREATE TABLE public.director_ (
    pid integer NOT NULL,
    mid integer NOT NULL
);
    DROP TABLE public.director_;
       public         heap r       postgres    false            �            1259    16500    genre_    TABLE     O   CREATE TABLE public.genre_ (
    genre_name text NOT NULL,
    content text
);
    DROP TABLE public.genre_;
       public         heap r       postgres    false            �            1259    16507 	   genre_of_    TABLE     Z   CREATE TABLE public.genre_of_ (
    genre_name text NOT NULL,
    mid integer NOT NULL
);
    DROP TABLE public.genre_of_;
       public         heap r       postgres    false            �            1259    16492    movie_    TABLE     �   CREATE TABLE public.movie_ (
    mid integer NOT NULL,
    title text NOT NULL,
    release_date date NOT NULL,
    plot text NOT NULL,
    num_reviews integer NOT NULL,
    rating_sum integer NOT NULL
);
    DROP TABLE public.movie_;
       public         heap r       postgres    false            �            1259    16491    movie__mid_seq    SEQUENCE     �   CREATE SEQUENCE public.movie__mid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.movie__mid_seq;
       public               postgres    false    223                       0    0    movie__mid_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.movie__mid_seq OWNED BY public.movie_.mid;
          public               postgres    false    222            �            1259    16515    person_    TABLE     �   CREATE TABLE public.person_ (
    pid integer NOT NULL,
    name text NOT NULL,
    dob date NOT NULL,
    description text NOT NULL
);
    DROP TABLE public.person_;
       public         heap r       postgres    false            �            1259    16514    person__pid_seq    SEQUENCE     �   CREATE SEQUENCE public.person__pid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.person__pid_seq;
       public               postgres    false    227            	           0    0    person__pid_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.person__pid_seq OWNED BY public.person_.pid;
          public               postgres    false    226            �            1259    16467    review_    TABLE     �   CREATE TABLE public.review_ (
    rid integer NOT NULL,
    uid integer NOT NULL,
    mid integer NOT NULL,
    comment text NOT NULL,
    rating double precision NOT NULL,
    date date NOT NULL,
    vote integer DEFAULT 0
);
    DROP TABLE public.review_;
       public         heap r       postgres    false            �            1259    16466    review__rid_seq    SEQUENCE     �   CREATE SEQUENCE public.review__rid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.review__rid_seq;
       public               postgres    false    220            
           0    0    review__rid_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.review__rid_seq OWNED BY public.review_.rid;
          public               postgres    false    219            �            1259    16458    user_    TABLE     �   CREATE TABLE public.user_ (
    uid integer NOT NULL,
    username character varying(50) NOT NULL,
    hash character varying(128) NOT NULL,
    join_date date NOT NULL,
    bio text NOT NULL
);
    DROP TABLE public.user_;
       public         heap r       postgres    false            �            1259    16457    user__uid_seq    SEQUENCE     �   CREATE SEQUENCE public.user__uid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.user__uid_seq;
       public               postgres    false    218                       0    0    user__uid_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.user__uid_seq OWNED BY public.user_.uid;
          public               postgres    false    217            �            1259    16476 
   user_votes    TABLE     r   CREATE TABLE public.user_votes (
    uid integer NOT NULL,
    rid integer NOT NULL,
    vote integer NOT NULL
);
    DROP TABLE public.user_votes;
       public         heap r       postgres    false            K           2604    16495 
   movie_ mid    DEFAULT     h   ALTER TABLE ONLY public.movie_ ALTER COLUMN mid SET DEFAULT nextval('public.movie__mid_seq'::regclass);
 9   ALTER TABLE public.movie_ ALTER COLUMN mid DROP DEFAULT;
       public               postgres    false    223    222    223            L           2604    16518    person_ pid    DEFAULT     j   ALTER TABLE ONLY public.person_ ALTER COLUMN pid SET DEFAULT nextval('public.person__pid_seq'::regclass);
 :   ALTER TABLE public.person_ ALTER COLUMN pid DROP DEFAULT;
       public               postgres    false    226    227    227            I           2604    16470    review_ rid    DEFAULT     j   ALTER TABLE ONLY public.review_ ALTER COLUMN rid SET DEFAULT nextval('public.review__rid_seq'::regclass);
 :   ALTER TABLE public.review_ ALTER COLUMN rid DROP DEFAULT;
       public               postgres    false    220    219    220            H           2604    16461 	   user_ uid    DEFAULT     f   ALTER TABLE ONLY public.user_ ALTER COLUMN uid SET DEFAULT nextval('public.user__uid_seq'::regclass);
 8   ALTER TABLE public.user_ ALTER COLUMN uid DROP DEFAULT;
       public               postgres    false    217    218    218            �          0    16523    cast_ 
   TABLE DATA           0   COPY public.cast_ (pid, mid, roles) FROM stdin;
    public               postgres    false    228   7                  0    16530    crew_ 
   TABLE DATA           )   COPY public.crew_ (pid, mid) FROM stdin;
    public               postgres    false    229   7                 0    16535 	   director_ 
   TABLE DATA           -   COPY public.director_ (pid, mid) FROM stdin;
    public               postgres    false    230   <7       �          0    16500    genre_ 
   TABLE DATA           5   COPY public.genre_ (genre_name, content) FROM stdin;
    public               postgres    false    224   Y7       �          0    16507 	   genre_of_ 
   TABLE DATA           4   COPY public.genre_of_ (genre_name, mid) FROM stdin;
    public               postgres    false    225   v7       �          0    16492    movie_ 
   TABLE DATA           Y   COPY public.movie_ (mid, title, release_date, plot, num_reviews, rating_sum) FROM stdin;
    public               postgres    false    223   �7       �          0    16515    person_ 
   TABLE DATA           >   COPY public.person_ (pid, name, dob, description) FROM stdin;
    public               postgres    false    227   =       �          0    16467    review_ 
   TABLE DATA           M   COPY public.review_ (rid, uid, mid, comment, rating, date, vote) FROM stdin;
    public               postgres    false    220   -=       �          0    16458    user_ 
   TABLE DATA           D   COPY public.user_ (uid, username, hash, join_date, bio) FROM stdin;
    public               postgres    false    218   �=       �          0    16476 
   user_votes 
   TABLE DATA           4   COPY public.user_votes (uid, rid, vote) FROM stdin;
    public               postgres    false    221   >                  0    0    movie__mid_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.movie__mid_seq', 12, true);
          public               postgres    false    222                       0    0    person__pid_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.person__pid_seq', 1, false);
          public               postgres    false    226                       0    0    review__rid_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.review__rid_seq', 3, true);
          public               postgres    false    219                       0    0    user__uid_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.user__uid_seq', 2, true);
          public               postgres    false    217            \           2606    16529    cast_ cast__pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.cast_
    ADD CONSTRAINT cast__pkey PRIMARY KEY (pid, mid);
 :   ALTER TABLE ONLY public.cast_ DROP CONSTRAINT cast__pkey;
       public                 postgres    false    228    228            ^           2606    16534    crew_ crew__pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.crew_
    ADD CONSTRAINT crew__pkey PRIMARY KEY (pid, mid);
 :   ALTER TABLE ONLY public.crew_ DROP CONSTRAINT crew__pkey;
       public                 postgres    false    229    229            `           2606    16539    director_ director__pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.director_
    ADD CONSTRAINT director__pkey PRIMARY KEY (pid, mid);
 B   ALTER TABLE ONLY public.director_ DROP CONSTRAINT director__pkey;
       public                 postgres    false    230    230            V           2606    16506    genre_ genre__pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.genre_
    ADD CONSTRAINT genre__pkey PRIMARY KEY (genre_name);
 <   ALTER TABLE ONLY public.genre_ DROP CONSTRAINT genre__pkey;
       public                 postgres    false    224            X           2606    16513    genre_of_ genre_of__pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.genre_of_
    ADD CONSTRAINT genre_of__pkey PRIMARY KEY (genre_name, mid);
 B   ALTER TABLE ONLY public.genre_of_ DROP CONSTRAINT genre_of__pkey;
       public                 postgres    false    225    225            T           2606    16499    movie_ movie__pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.movie_
    ADD CONSTRAINT movie__pkey PRIMARY KEY (mid);
 <   ALTER TABLE ONLY public.movie_ DROP CONSTRAINT movie__pkey;
       public                 postgres    false    223            Z           2606    16522    person_ person__pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.person_
    ADD CONSTRAINT person__pkey PRIMARY KEY (pid);
 >   ALTER TABLE ONLY public.person_ DROP CONSTRAINT person__pkey;
       public                 postgres    false    227            P           2606    16475    review_ review__pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.review_
    ADD CONSTRAINT review__pkey PRIMARY KEY (rid);
 >   ALTER TABLE ONLY public.review_ DROP CONSTRAINT review__pkey;
       public                 postgres    false    220            N           2606    16465    user_ user__pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.user_
    ADD CONSTRAINT user__pkey PRIMARY KEY (uid);
 :   ALTER TABLE ONLY public.user_ DROP CONSTRAINT user__pkey;
       public                 postgres    false    218            R           2606    16480    user_votes user_votes_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.user_votes
    ADD CONSTRAINT user_votes_pkey PRIMARY KEY (uid, rid);
 D   ALTER TABLE ONLY public.user_votes DROP CONSTRAINT user_votes_pkey;
       public                 postgres    false    221    221            a           2606    16486    user_votes user_votes_rid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_votes
    ADD CONSTRAINT user_votes_rid_fkey FOREIGN KEY (rid) REFERENCES public.review_(rid) ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.user_votes DROP CONSTRAINT user_votes_rid_fkey;
       public               postgres    false    220    221    4688            b           2606    16481    user_votes user_votes_uid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_votes
    ADD CONSTRAINT user_votes_uid_fkey FOREIGN KEY (uid) REFERENCES public.user_(uid) ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.user_votes DROP CONSTRAINT user_votes_uid_fkey;
       public               postgres    false    218    4686    221            �      x������ � �             x������ � �            x������ � �      �      x������ � �      �      x������ � �      �   m  x�UVMs�6=ӿb'�\D�(�Nݛ��i;�$w�K/+rI� Jf}�r29I"��x��[5՝�ˮ��~�W�~�w7�G��;J��Ab��Xk�@GӉx�ޙHlm�6�j����zo�?���'�=M&�&E��#M�)�Q^� �`����i�����gY����ăq|�B�?I�V�jw����I��(hhw]������k"�@\����q*��4�	�������p��Z4��"k�(hC<A��5�V�J�������k>@��i�pk-!��jE�}�S��[4�uVj ��M;Mf�O2'Zf2]��gd��cl2�H��x��\FR^�CV:��1[�2���B�
�`<���;'�^�L3�ho5n��Ѩ1�t��w@T�+"�K�t�����;n4yb��l��8K�$:�~��0ZKX'��T�x� �����8H*dy�Kp�h_��HHs.��>���q���A�ܖ��Bs3k�4�eMĽG�=��h}4S���z���P?���n��c�����
����V���������-'����	l��1,�8��H�����loGʗ<&���cS=)�~L}K��R��^�Gr�'�a�Ԭ*�	~�J��ڧ%&̢��D��I4	���Aom����
w HϚ�W��\�usU�BZ؁��`n��� �Ppo�hF�ga
���*�1��`�����Ej/�q��@����_��sd�������칍 �kgZ�,�������W57�M���}�(�a�zT��N3�4y֊Eb�Ҁ N�����j��"!������l����`��=OƮ��������z�]��]�3�r=H+Y�p�U]���6?�w4��G�@S�D�}����Vu�����7�Sn��"��ϊ�hX1U�7yi\��L8&?cb1�-Ϩ��M�TW5f♙�^�g
��zTi52p��84*k��3{�4ٚ���b!7��I�����&�Iy���h�l>�����m4�F��E��(�;��E菾,I��R�77�m&튾�Ŭ��=B���Ҕc>��)��%;������+u�̛|X&�ӉT�~��=��Э�?�8(��;�#�շ{k��*j��?5[�ݚ�xy�mr�؎��s�Mu:sL�����{�r���_U���pе���.Ϋ5D�BmX�v���0aݛ.�h�u3�b)��9l�4��W�)��<�����lMf�j����h��@�ӵ�\CX���	�<[�f��L�q�O�Վ��SG�i.^��y�<���C2��p�����*�˲�vn��=�������-;GM��`g��½<��W@�'�w(T�G8��?���]�������mM�      �      x������ � �      �   W   x�]ʻ�0��y
SQ��;P&(.��"�;�@+'���Y�̾����Fu
�!.��&�V?���^J#�Y�������6�4��      �   z   x���;�0@g�� ��ĉ��Ub�:�䇊�X`��e�	*=��-����;��siI�W�V�J*Z+�:�L9�j�kA�S��D���Y���`y� ��z��l�~���m}��i2?��@�/�4      �   "   x�3�4�4�2�4�F@RD�9�@2F��� O�H     