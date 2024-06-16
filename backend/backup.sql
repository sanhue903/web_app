PGDMP      2                |            memoria    16.3    16.3 9    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    25293    memoria    DATABASE     �   CREATE DATABASE memoria WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE memoria;
                postgres    false            �            1259    25305    application    TABLE     o   CREATE TABLE public.application (
    id character varying(6) NOT NULL,
    name character varying NOT NULL
);
    DROP TABLE public.application;
       public         heap    postgres    false            �            1259    25313    aule    TABLE     }   CREATE TABLE public.aule (
    id integer NOT NULL,
    name character varying(15) NOT NULL,
    user_id integer NOT NULL
);
    DROP TABLE public.aule;
       public         heap    postgres    false            �            1259    25312    aule_id_seq    SEQUENCE     �   CREATE SEQUENCE public.aule_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.aule_id_seq;
       public          postgres    false    219            �           0    0    aule_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE public.aule_id_seq OWNED BY public.aule.id;
          public          postgres    false    218            �            1259    25361    aule_student_relationship    TABLE     �   CREATE TABLE public.aule_student_relationship (
    id integer NOT NULL,
    aule_id integer NOT NULL,
    student_id integer NOT NULL
);
 -   DROP TABLE public.aule_student_relationship;
       public         heap    postgres    false            �            1259    25360     aule_student_relationship_id_seq    SEQUENCE     �   CREATE SEQUENCE public.aule_student_relationship_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.aule_student_relationship_id_seq;
       public          postgres    false    225            �           0    0     aule_student_relationship_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.aule_student_relationship_id_seq OWNED BY public.aule_student_relationship.id;
          public          postgres    false    224            �            1259    25336    chapter    TABLE     �   CREATE TABLE public.chapter (
    id character varying(6) NOT NULL,
    name character varying NOT NULL,
    number integer NOT NULL,
    app_id character varying(6) NOT NULL
);
    DROP TABLE public.chapter;
       public         heap    postgres    false            �            1259    25348    question    TABLE     �   CREATE TABLE public.question (
    id character varying(6) NOT NULL,
    text character varying NOT NULL,
    chapter_id character varying(6) NOT NULL,
    number integer NOT NULL
);
    DROP TABLE public.question;
       public         heap    postgres    false            �            1259    25378    score    TABLE     l  CREATE TABLE public.score (
    id integer NOT NULL,
    answer character varying NOT NULL,
    seconds double precision NOT NULL,
    is_correct boolean NOT NULL,
    date timestamp with time zone DEFAULT now() NOT NULL,
    attempt integer NOT NULL,
    session integer NOT NULL,
    student_id integer NOT NULL,
    question_id character varying(6) NOT NULL
);
    DROP TABLE public.score;
       public         heap    postgres    false            �            1259    25377    score_id_seq    SEQUENCE     �   CREATE SEQUENCE public.score_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.score_id_seq;
       public          postgres    false    227            �           0    0    score_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.score_id_seq OWNED BY public.score.id;
          public          postgres    false    226            �            1259    25325    student    TABLE     �   CREATE TABLE public.student (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    age integer NOT NULL,
    session integer NOT NULL,
    app_id character varying(6) NOT NULL
);
    DROP TABLE public.student;
       public         heap    postgres    false            �            1259    25324    student_id_seq    SEQUENCE     �   CREATE SEQUENCE public.student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.student_id_seq;
       public          postgres    false    221            �           0    0    student_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.student_id_seq OWNED BY public.student.id;
          public          postgres    false    220            �            1259    25295    user    TABLE     �   CREATE TABLE public."user" (
    id integer NOT NULL,
    email character varying(50) NOT NULL,
    password character varying NOT NULL,
    is_admin boolean NOT NULL
);
    DROP TABLE public."user";
       public         heap    postgres    false            �            1259    25294    user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.user_id_seq;
       public          postgres    false    216                        0    0    user_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;
          public          postgres    false    215            ;           2604    25316    aule id    DEFAULT     b   ALTER TABLE ONLY public.aule ALTER COLUMN id SET DEFAULT nextval('public.aule_id_seq'::regclass);
 6   ALTER TABLE public.aule ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    218    219            =           2604    25364    aule_student_relationship id    DEFAULT     �   ALTER TABLE ONLY public.aule_student_relationship ALTER COLUMN id SET DEFAULT nextval('public.aule_student_relationship_id_seq'::regclass);
 K   ALTER TABLE public.aule_student_relationship ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    225    225            >           2604    25381    score id    DEFAULT     d   ALTER TABLE ONLY public.score ALTER COLUMN id SET DEFAULT nextval('public.score_id_seq'::regclass);
 7   ALTER TABLE public.score ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    227    227            <           2604    25328 
   student id    DEFAULT     h   ALTER TABLE ONLY public.student ALTER COLUMN id SET DEFAULT nextval('public.student_id_seq'::regclass);
 9   ALTER TABLE public.student ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    220    221            :           2604    25298    user id    DEFAULT     d   ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);
 8   ALTER TABLE public."user" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    215    216            �          0    25305    application 
   TABLE DATA           /   COPY public.application (id, name) FROM stdin;
    public          postgres    false    217   JA       �          0    25313    aule 
   TABLE DATA           1   COPY public.aule (id, name, user_id) FROM stdin;
    public          postgres    false    219   �A       �          0    25361    aule_student_relationship 
   TABLE DATA           L   COPY public.aule_student_relationship (id, aule_id, student_id) FROM stdin;
    public          postgres    false    225   �A       �          0    25336    chapter 
   TABLE DATA           ;   COPY public.chapter (id, name, number, app_id) FROM stdin;
    public          postgres    false    222   �A       �          0    25348    question 
   TABLE DATA           @   COPY public.question (id, text, chapter_id, number) FROM stdin;
    public          postgres    false    223   ;B       �          0    25378    score 
   TABLE DATA           q   COPY public.score (id, answer, seconds, is_correct, date, attempt, session, student_id, question_id) FROM stdin;
    public          postgres    false    227   �C       �          0    25325    student 
   TABLE DATA           A   COPY public.student (id, name, age, session, app_id) FROM stdin;
    public          postgres    false    221   �G       �          0    25295    user 
   TABLE DATA           ?   COPY public."user" (id, email, password, is_admin) FROM stdin;
    public          postgres    false    216   �H                  0    0    aule_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.aule_id_seq', 1, false);
          public          postgres    false    218                       0    0     aule_student_relationship_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.aule_student_relationship_id_seq', 1, false);
          public          postgres    false    224                       0    0    score_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.score_id_seq', 18, true);
          public          postgres    false    226                       0    0    student_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.student_id_seq', 27, true);
          public          postgres    false    220                       0    0    user_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.user_id_seq', 1, false);
          public          postgres    false    215            E           2606    25311    application application_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.application
    ADD CONSTRAINT application_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.application DROP CONSTRAINT application_pkey;
       public            postgres    false    217            G           2606    25318    aule aule_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.aule
    ADD CONSTRAINT aule_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.aule DROP CONSTRAINT aule_pkey;
       public            postgres    false    219            O           2606    25366 8   aule_student_relationship aule_student_relationship_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.aule_student_relationship
    ADD CONSTRAINT aule_student_relationship_pkey PRIMARY KEY (id);
 b   ALTER TABLE ONLY public.aule_student_relationship DROP CONSTRAINT aule_student_relationship_pkey;
       public            postgres    false    225            K           2606    25342    chapter chapter_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.chapter
    ADD CONSTRAINT chapter_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.chapter DROP CONSTRAINT chapter_pkey;
       public            postgres    false    222            M           2606    25354    question question_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.question DROP CONSTRAINT question_pkey;
       public            postgres    false    223            Q           2606    25386    score score_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.score
    ADD CONSTRAINT score_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.score DROP CONSTRAINT score_pkey;
       public            postgres    false    227            I           2606    25330    student student_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.student DROP CONSTRAINT student_pkey;
       public            postgres    false    221            A           2606    25304    user user_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_email_key;
       public            postgres    false    216            C           2606    25302    user user_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public            postgres    false    216            V           2606    25367 @   aule_student_relationship aule_student_relationship_aule_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.aule_student_relationship
    ADD CONSTRAINT aule_student_relationship_aule_id_fkey FOREIGN KEY (aule_id) REFERENCES public.aule(id);
 j   ALTER TABLE ONLY public.aule_student_relationship DROP CONSTRAINT aule_student_relationship_aule_id_fkey;
       public          postgres    false    225    219    4679            W           2606    25372 C   aule_student_relationship aule_student_relationship_student_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.aule_student_relationship
    ADD CONSTRAINT aule_student_relationship_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.student(id);
 m   ALTER TABLE ONLY public.aule_student_relationship DROP CONSTRAINT aule_student_relationship_student_id_fkey;
       public          postgres    false    225    221    4681            R           2606    25319    aule aule_user_id_fkey    FK CONSTRAINT     v   ALTER TABLE ONLY public.aule
    ADD CONSTRAINT aule_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);
 @   ALTER TABLE ONLY public.aule DROP CONSTRAINT aule_user_id_fkey;
       public          postgres    false    219    216    4675            T           2606    25343    chapter chapter_app_id_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.chapter
    ADD CONSTRAINT chapter_app_id_fkey FOREIGN KEY (app_id) REFERENCES public.application(id);
 E   ALTER TABLE ONLY public.chapter DROP CONSTRAINT chapter_app_id_fkey;
       public          postgres    false    4677    222    217            U           2606    25355 !   question question_chapter_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_chapter_id_fkey FOREIGN KEY (chapter_id) REFERENCES public.chapter(id);
 K   ALTER TABLE ONLY public.question DROP CONSTRAINT question_chapter_id_fkey;
       public          postgres    false    222    4683    223            X           2606    25392    score score_question_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.score
    ADD CONSTRAINT score_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.question(id);
 F   ALTER TABLE ONLY public.score DROP CONSTRAINT score_question_id_fkey;
       public          postgres    false    227    4685    223            Y           2606    25387    score score_student_id_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.score
    ADD CONSTRAINT score_student_id_fkey FOREIGN KEY (student_id) REFERENCES public.student(id);
 E   ALTER TABLE ONLY public.score DROP CONSTRAINT score_student_id_fkey;
       public          postgres    false    221    227    4681            S           2606    25331    student student_app_id_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_app_id_fkey FOREIGN KEY (app_id) REFERENCES public.application(id);
 E   ALTER TABLE ONLY public.student DROP CONSTRAINT student_app_id_fkey;
       public          postgres    false    221    217    4677            �   1   x�s����t�Qp�/�,,��SHIU�I,Vp��O���K-����� �      �      x������ � �      �      x������ � �      �   f   x�s��s���t��K�L�D��������NCN'��@O� Ww�����Ҝ���Û�T�T9���T9�����碘dS��� �.� ��>��=... �0*      �   I  x�m�MN�0���)� )�ۢ
�AB�;6�xh]9��q*�۰�U�D.�8n�.�b���}��e��rW��ߟ��T3��E�����@��&ؚ��m,�LV�~x��EڔS�<�����# 
�ZJ�V�X�mw:�8��i&͔��A�U� 2TY�T5K4�d9��e��@�n8D��z�)v��4���D���BJ�{
�48�̳�⿔[\;\+��{�d��4�c� ���}�."�T| ��'{r��Ȫ��9�8�u񹋜d94��:�%yΎj�A��.��v�	{�:�A�.Cu�%�kʶ��v����x�.��$��      �   Q  x���K��6D��)p�f�����o`！H�`��; ��i�v�b��z��J@0���<�xyճ�A-|�Re#�3_d�>X�*���:p#'m��O��AG.�_)D��Ϛ��ݬ��l<U�в��cݾ�7�q1���{�Vm/1�[&����h5�.�"��N|r��f�W(��7ڳ�v��^5�6���|U�bc]5Ǒ}� �� ��aƝ����R?ePƤp�oF(բZV|u�W��m��2:0!��}Y����-�kH�V-�8vB;�3�Yd����<}�&�HV�>��Iq�č>+�Oї�o��*�ں:�����#h�f=Ŵ@i�g��2]P/�=�f�q�Q*��5E�ќx����p�޴�����J<!B^D���YWW��úG���~(�`E,^�k�oO�"�\��w�e�"s��.���r�/q�G�,[�QCB��dJ��|��a�� F� j��Ha������y+���3kY?V��_b�sxb��z��و��?in�!��d�3��W�aळ6����gs���&8�QRo��O[�J8'���e�k�?�8V�xz��ӣ�#+�D���0À?�����Gk2W�8�O��<�k��f��� /:R'(w6�Q!�VC7�Tz|TZ�Mg�jB����&Ճ5��M~2��G��X���a@�[�� D���Y�k2k�>WF�ÐC�_��T5���4dL�zn�%�(��T�/�D�ڿ��c#�a�`"'q��f{,PjA�����&�"s'�H���%u2�����D�������|f�]%��5l}���+K�����l�34ǅ+#��xJI�֙�J1�\J��l��NMu�7�5wq��S��e��<҅�vh<ų��{ṙ�w �z��F_R�컦�OM=����o���ڧ�w�?���b}U�����|JaU��@׬�qO�_K�=Iܳ:8m���uY��f�)�Hk�|9�7P�c�6�w ]_uMݜ����ʰ gJ2�B]\��*d�흇�/M�A���s�(�FA��x��=�s0[���P5�77��������}�������i�o��D�G�?����7��o�      �   �   x���;n�0��>�N��+�N	��N]�Fm(b+[|��%k���j#�� A�z3�8���T��̌�K����9n�2YTɢ��?UG��؋]�c#a+���B���W�q���\�B0-X	k7�#V��=q������hFw�@s���K	W���3�^�Zt�\�t�,�d�a�W2U��9��w������'Vk?�g0c�M�[ًGo]�o�,�~ cG�      �      x������ � �     