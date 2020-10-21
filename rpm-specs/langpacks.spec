Name:      langpacks
Version:   3.0
Release:   5%{?dist}
Summary:   Langpacks meta-package

License:   GPLv2+
BuildArch: noarch
BuildRequires: python3 fontconfig
# Below Source was available on https://people.freedesktop.org/~hughsient/temp/
Source0:   org.fedoraproject.LangPacks.xml
Source1:   org.fedoraproject.LangPacks-Core.xml
Source2:   org.fedoraproject.LangPacks-Core-Font.xml
Source3:   normlang.py

# to split up the AppStream file
BuildRequires: libappstream-glib >= 0.5.10

%description
Langpack meta-package to provide individual langpacks packages.

# The following language list is generated based on
# 1) take the languages where anaconda translations are available
# ls /usr/share/locale/*/LC_MESSAGES/anaconda.mo
# Then pick those languages which provides at least a single langpack
# Now, Added exception for dz and ku languages which have no anaconda.mo
# 2) Added br ga he nn nr ss tn ts ve xh
# as per requested in https://bugzilla.redhat.com/show_bug.cgi?id=1310538
# 3) Enabled en langpack https://bugzilla.redhat.com/show_bug.cgi?id=1312890


# langcore_pkg (defaultime,defaultfont,langcode,langname)
%define langcore_pkg(i:f:l:n:) \
%define langcode %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
%define normcode %{lua:print((string.gsub(string.lower(rpm.expand("%{langcode}")), "_","-")))}\
%define langortho %(python3 %{SOURCE3} %{langcode}) \
%define lowerortho %{lua:print(string.lower(rpm.expand("%{langortho}")))}\
%define fontpkgcode %{lua:print((string.gsub(rpm.expand("%{langortho}"),"-","_")))}\
\
%package core-%{langcode}\
Summary: %{langname} langpacks core meta-package\
Requires: langpacks-core-font-%{fontpkgcode}\
%{-i:Requires: (%{-i*} if xorg-x11-server-Xorg)} \
\
%description core-%{langcode}\
This package provides %{langname} core langpacks packages.\
\
%files core-%{langcode}\
%{_datadir}/metainfo/org.fedoraproject.LangPack-Core-%{langcode}.metainfo.xml\
\
%if "%{normcode}" == "%{lowerortho}"\
%package core-font-%{fontpkgcode}\
Summary: %{langname} core font meta-package\
%{-f:Requires: %{-f*}}%{!-f:Requires: dejavu-sans-fonts} \
%{-l:Provides: font(:lang=%{lowerortho})}  \
%if "%{lowerortho}" != "%{fontpkgcode}"\
Provides: langpacks-core-font-%{lowerortho} = %{version}-%{release} \
Obsoletes: langpacks-core-font-%{lowerortho} < %{version}-%{release} \
%endif \
\
%description core-font-%{fontpkgcode}\
This package defines the default font for %{langname} language.\
\
%files core-font-%{fontpkgcode}\
%{_datadir}/metainfo/org.fedoraproject.LangPack-Core-Font-%{fontpkgcode}.metainfo.xml\
%endif

%package af
Summary: Afrikaans langpacks meta-package
Requires: %{name}-core-af

%description af
This package provides Afrikaans langpacks meta-package.

%files af
%{_datadir}/metainfo/org.fedoraproject.LangPack-af.metainfo.xml

%langcore_pkg -l af -n Afrikaans

%package am
Summary: Amharic langpacks meta-package
Requires: %{name}-core-am
Recommends: senamirmir-washra-fantuwua-fonts
Recommends: senamirmir-washra-fonts
Recommends: senamirmir-washra-hiwua-fonts
Recommends: senamirmir-washra-jiret-fonts
Recommends: senamirmir-washra-tint-fonts
Recommends: senamirmir-washra-wookianos-fonts
Recommends: senamirmir-washra-yebse-fonts
Recommends: senamirmir-washra-yigezu-bisrat-goffer-fonts
Recommends: senamirmir-washra-yigezu-bisrat-gothic-fonts
Recommends: senamirmir-washra-zelan-fonts
Recommends: xorg-x11-fonts-ethiopic
Recommends: google-noto-sans-ethiopic-vf-fonts

%description am
This package provides Amharic langpacks meta-package.

%files am
%{_datadir}/metainfo/org.fedoraproject.LangPack-am.metainfo.xml

%langcore_pkg -l am -n Amharic -f sil-abyssinica-fonts

%package ar
Summary: Arabic langpacks meta-package
Requires: %{name}-core-ar
Recommends: dejavu-sans-mono-fonts
Recommends: kacst-art-fonts
Recommends: kacst-book-fonts
Recommends: kacst-decorative-fonts
Recommends: kacst-digital-fonts
Recommends: kacst-farsi-fonts
Recommends: kacst-letter-fonts
Recommends: kacst-naskh-fonts
Recommends: kacst-office-fonts
Recommends: kacst-one-fonts
Recommends: kacst-pen-fonts
Recommends: kacst-poster-fonts
Recommends: kacst-qurn-fonts
Recommends: kacst-screen-fonts
Recommends: kacst-title-fonts
Recommends: kacst-titlel-fonts
Recommends: paktype-naqsh-fonts
Recommends: paktype-tehreer-fonts

%description ar
This package provides Arabic langpacks meta-package.

%files ar
%{_datadir}/metainfo/org.fedoraproject.LangPack-ar.metainfo.xml

%langcore_pkg -l ar -n Arabic

%package as
Summary: Assamese langpacks meta-package
Requires: %{name}-core-as
Recommends: google-noto-sans-bengali-vf-fonts
Recommends: google-noto-sans-bengali-ui-vf-fonts

%description as
This package provides Assamese langpacks meta-package.

%files as
%{_datadir}/metainfo/org.fedoraproject.LangPack-as.metainfo.xml

%langcore_pkg -l as -n Assamese -f lohit-assamese-fonts -i ibus-m17n

%package ast
Summary: Asturian langpacks meta-package
Requires: %{name}-core-ast
Recommends: dejavu-sans-fonts

%description ast
This package provides Asturian langpacks meta-package.

%files ast
%{_datadir}/metainfo/org.fedoraproject.LangPack-ast.metainfo.xml

%langcore_pkg -l ast -n Asturian

%package be
Summary: Belarusian langpacks meta-package
Requires: %{name}-core-be

%description be
This package provides Belarusian langpacks meta-package.

%files be
%{_datadir}/metainfo/org.fedoraproject.LangPack-be.metainfo.xml

%langcore_pkg -l be -n Belarusian

%package bg
Summary: Bulgarian langpacks meta-package
Requires: %{name}-core-bg

%description bg
This package provides Bulgarian langpacks meta-package.

%files bg
%{_datadir}/metainfo/org.fedoraproject.LangPack-bg.metainfo.xml

%langcore_pkg -l bg -n Bulgarian

%package bn
Summary: Bengali langpacks meta-package
Requires: %{name}-core-bn
Recommends: google-noto-sans-bengali-vf-fonts
Recommends: google-noto-sans-bengali-ui-vf-fonts

%description bn
This package provides Bengali langpacks meta-package.

%files bn
%{_datadir}/metainfo/org.fedoraproject.LangPack-bn.metainfo.xml

%langcore_pkg -l bn -n Bengali -f lohit-bengali-fonts -i ibus-m17n

%package bo
Summary: Tibetan langpacks meta-package
Requires: %{name}-core-bo
Recommends: tibetan-machine-uni-fonts

%description bo
This package provides Tibetan langpacks meta-package.

%files bo
%{_datadir}/metainfo/org.fedoraproject.LangPack-bo.metainfo.xml

%langcore_pkg -l bo -n Tibetan -f jomolhari-fonts -i ibus-m17n

%package br
Summary: Breton langpacks meta-package
Requires: %{name}-core-br

%description br
This package provides Breton langpacks meta-package.

%files br
%{_datadir}/metainfo/org.fedoraproject.LangPack-br.metainfo.xml

%langcore_pkg -l br -n Breton

%package bs
Summary: Bosnian langpacks meta-package
Requires: %{name}-core-bs

%description bs
This package provides Bosnian langpacks meta-package.

%files bs
%{_datadir}/metainfo/org.fedoraproject.LangPack-bs.metainfo.xml

%langcore_pkg -l bs -n Bosnian

%package ca
Summary: Catalan langpacks meta-package
Requires: %{name}-core-ca

%description ca
This package provides Catalan langpacks meta-package.

%files ca
%{_datadir}/metainfo/org.fedoraproject.LangPack-ca.metainfo.xml

%langcore_pkg -l ca -n Catalan

%package cs
Summary: Czech langpacks meta-package
Requires: %{name}-core-cs

%description cs
This package provides Czech langpacks meta-package.

%files cs
%{_datadir}/metainfo/org.fedoraproject.LangPack-cs.metainfo.xml

%langcore_pkg -l cs -n Czech

%package cy
Summary: Welsh langpacks meta-package
Requires: %{name}-core-cy

%description cy
This package provides Welsh langpacks meta-package.

%files cy
%{_datadir}/metainfo/org.fedoraproject.LangPack-cy.metainfo.xml

%langcore_pkg -l cy -n Welsh

%package da
Summary: Danish langpacks meta-package
Requires: %{name}-core-da

%description da
This package provides Danish langpacks meta-package.

%files da
%{_datadir}/metainfo/org.fedoraproject.LangPack-da.metainfo.xml

%langcore_pkg -l da -n Danish

%package de
Summary: German langpacks meta-package
Requires: %{name}-core-de

%description de
This package provides German langpacks meta-package.

%files de
%{_datadir}/metainfo/org.fedoraproject.LangPack-de.metainfo.xml

%langcore_pkg -l de -n German

%package dz
Summary: Bhutanese langpacks meta-package
Requires: %{name}-core-dz

%description dz
This package provides Bhutanese langpacks meta-package.

%files dz
%{_datadir}/metainfo/org.fedoraproject.LangPack-dz.metainfo.xml

%langcore_pkg -l dz -n Bhutanese

%package el
Summary: Greek langpacks meta-package
Requires: %{name}-core-el

%description el
This package provides Greek langpacks meta-package.

%files el
%{_datadir}/metainfo/org.fedoraproject.LangPack-el.metainfo.xml

%langcore_pkg -l el -n Greek

%package en
Summary: English langpacks meta-package
Requires: %{name}-core-en

%description en
This package provides English langpacks meta-package.

%files en
%{_datadir}/metainfo/org.fedoraproject.LangPack-en.metainfo.xml

%langcore_pkg -l en -n English

%package en_GB
Summary: English (United Kingdom) langpacks meta-package
Requires: %{name}-core-en_GB

%description en_GB
This package provides English (United Kingdom) langpacks meta-package.

%files en_GB
%{_datadir}/metainfo/org.fedoraproject.LangPack-en_GB.metainfo.xml

%langcore_pkg -l en_GB -n %{quote:English (United Kingdom)}

%package eo
Summary: Esperanto langpacks meta-package
Requires: %{name}-core-eo

%description eo
This package provides Esperanto langpacks meta-package.

%files eo
%{_datadir}/metainfo/org.fedoraproject.LangPack-eo.metainfo.xml

%langcore_pkg -l eo -n Esperanto

%package es
Summary: Spanish langpacks meta-package
Requires: %{name}-core-es

%description es
This package provides Spanish langpacks meta-package.

%files es
%{_datadir}/metainfo/org.fedoraproject.LangPack-es.metainfo.xml

%langcore_pkg -l es -n Spanish

%package et
Summary: Estonian langpacks meta-package
Requires: %{name}-core-et

%description et
This package provides Estonian langpacks meta-package.

%files et
%{_datadir}/metainfo/org.fedoraproject.LangPack-et.metainfo.xml

%langcore_pkg -l et -n Estonian

%package eu
Summary: Basque langpacks meta-package
Requires: %{name}-core-eu

%description eu
This package provides Basque langpacks meta-package.

%files eu
%{_datadir}/metainfo/org.fedoraproject.LangPack-eu.metainfo.xml

%langcore_pkg -l eu -n Basque

%package fa
Summary: Persian langpacks meta-package
Requires: %{name}-core-fa

%description fa
This package provides Persian langpacks meta-package.

%files fa
%{_datadir}/metainfo/org.fedoraproject.LangPack-fa.metainfo.xml

%langcore_pkg -l fa -n Persian

%package fi
Summary: Finnish langpacks meta-package
Requires: %{name}-core-fi

%description fi
This package provides Finnish langpacks meta-package.

%files fi
%{_datadir}/metainfo/org.fedoraproject.LangPack-fi.metainfo.xml

%langcore_pkg -l fi -n Finnish

%package fr
Summary: French langpacks meta-package
Requires: %{name}-core-fr

%description fr
This package provides French langpacks meta-package.

%files fr
%{_datadir}/metainfo/org.fedoraproject.LangPack-fr.metainfo.xml

%langcore_pkg -l fr -n French

%package ga
Summary: Irish langpacks meta-package
Requires: %{name}-core-ga

%description ga
This package provides Irish langpacks meta-package.

%files ga
%{_datadir}/metainfo/org.fedoraproject.LangPack-ga.metainfo.xml

%langcore_pkg -l ga -n Irish

%package gl
Summary: Galician langpacks meta-package
Requires: %{name}-core-gl

%description gl
This package provides Galician langpacks meta-package.

%files gl
%{_datadir}/metainfo/org.fedoraproject.LangPack-gl.metainfo.xml

%langcore_pkg -l gl -n Galician

%package gu
Summary: Gujarati langpacks meta-package
Requires: %{name}-core-gu
Recommends: google-noto-sans-gujarati-fonts
Recommends: google-noto-sans-gujarati-ui-fonts
Recommends: samyak-gujarati-fonts

%description gu
This package provides Gujarati langpacks meta-package.

%files gu
%{_datadir}/metainfo/org.fedoraproject.LangPack-gu.metainfo.xml

%langcore_pkg -l gu -n Gujarati -f lohit-gujarati-fonts -i ibus-m17n

%package he
Summary: Hebrew langpacks meta-package
Requires: %{name}-core-he
Recommends: culmus-aharoni-clm-fonts
Recommends: culmus-caladings-clm-fonts
Recommends: culmus-david-clm-fonts
Recommends: culmus-drugulin-clm-fonts
Recommends: culmus-ellinia-clm-fonts
Recommends: culmus-frank-ruehl-clm-fonts
Recommends: culmus-hadasim-clm-fonts
Recommends: culmus-keteryg-fonts
Recommends: culmus-miriam-clm-fonts
Recommends: culmus-miriam-mono-clm-fonts
Recommends: culmus-nachlieli-clm-fonts
Recommends: culmus-simple-clm-fonts
Recommends: culmus-stamashkenaz-clm-fonts
Recommends: culmus-stamsefarad-clm-fonts
Recommends: culmus-yehuda-clm-fonts
Recommends: google-noto-sans-hebrew-vf-fonts

%description he
This package provides Hebrew langpacks meta-package.

%files he
%{_datadir}/metainfo/org.fedoraproject.LangPack-he.metainfo.xml

%langcore_pkg -l he -n Hebrew

%package hi
Summary: Hindi langpacks meta-package
Requires: %{name}-core-hi
Recommends: google-noto-sans-devanagari-vf-fonts
Recommends: google-noto-sans-devanagari-ui-vf-fonts
Recommends: samyak-devanagari-fonts

%description hi
This package provides Hindi langpacks meta-package.

%files hi
%{_datadir}/metainfo/org.fedoraproject.LangPack-hi.metainfo.xml

%langcore_pkg -l hi -n Hindi -f lohit-devanagari-fonts -i ibus-m17n

%package hr
Summary: Croatian langpacks meta-package
Requires: %{name}-core-hr

%description hr
This package provides Croatian langpacks meta-package.

%files hr
%{_datadir}/metainfo/org.fedoraproject.LangPack-hr.metainfo.xml

%langcore_pkg -l hr -n Croatian

%package hu
Summary: Hungarian langpacks meta-package
Requires: %{name}-core-hu

%description hu
This package provides Hungarian langpacks meta-package.

%files hu
%{_datadir}/metainfo/org.fedoraproject.LangPack-hu.metainfo.xml

%langcore_pkg -l hu -n Hungarian

%package ia
Summary: Interlingua langpacks meta-package
Requires: %{name}-core-ia

%description ia
This package provides Interlingua langpacks meta-package.

%files ia
%{_datadir}/metainfo/org.fedoraproject.LangPack-ia.metainfo.xml

%langcore_pkg -l ia -n Interlingua

%package id
Summary: Indonesian langpacks meta-package
Requires: %{name}-core-id

%description id
This package provides Indonesian langpacks meta-package.

%files id
%{_datadir}/metainfo/org.fedoraproject.LangPack-id.metainfo.xml

%langcore_pkg -l id -n Indonesian

%package is
Summary: Icelandic langpacks meta-package
Requires: %{name}-core-is

%description is
This package provides Icelandic langpacks meta-package.

%files is
%{_datadir}/metainfo/org.fedoraproject.LangPack-is.metainfo.xml

%langcore_pkg -l is -n Icelandic

%package it
Summary: Italian langpacks meta-package
Requires: %{name}-core-it

%description it
This package provides Italian langpacks meta-package.

%files it
%{_datadir}/metainfo/org.fedoraproject.LangPack-it.metainfo.xml

%langcore_pkg -l it -n Italian

%package ja
Summary: Japanese langpacks meta-package
Requires: %{name}-core-ja
Recommends: google-noto-serif-cjk-ttc-fonts
Recommends: (uim-anthy if uim)

%description ja
This package provides Japanese langpacks meta-package.

%files ja
%{_datadir}/metainfo/org.fedoraproject.LangPack-ja.metainfo.xml

%langcore_pkg -l ja -n Japanese -f google-noto-sans-cjk-ttc-fonts -i ibus-kkc

%package ka
Summary: Georgian langpacks meta-package
Requires: %{name}-core-ka
Recommends: bpg-chveulebrivi-fonts
Recommends: bpg-courier-fonts
Recommends: bpg-glaho-fonts
Recommends: dejavu-sans-mono-fonts
Recommends: dejavu-serif-fonts
Recommends: google-noto-sans-georgian-vf-fonts
Recommends: google-noto-serif-georgian-vf-fonts

%description ka
This package provides Georgian langpacks meta-package.

%files ka
%{_datadir}/metainfo/org.fedoraproject.LangPack-ka.metainfo.xml

%langcore_pkg -l ka -n Georgian

%package kk
Summary: Kazakh langpacks meta-package
Requires: %{name}-core-kk

%description kk
This package provides Kazakh langpacks meta-package.

%files kk
%{_datadir}/metainfo/org.fedoraproject.LangPack-kk.metainfo.xml

%langcore_pkg -l kk -n Kazakh

%package km
Summary: Khmer langpacks meta-package
Requires: %{name}-core-km
Recommends: google-noto-sans-khmer-vf-fonts
Recommends: google-noto-sans-khmer-ui-vf-fonts
Recommends: khmer-os-battambang-fonts
Recommends: khmer-os-bokor-fonts
Recommends: khmer-os-content-fonts
Recommends: khmer-os-fasthand-fonts
Recommends: khmer-os-freehand-fonts
Recommends: khmer-os-handwritten-fonts
Recommends: khmer-os-metal-chrieng-fonts
Recommends: khmer-os-muol-fonts-all
Recommends: khmer-os-siemreap-fonts

%description km
This package provides Khmer langpacks meta-package.

%files km
%{_datadir}/metainfo/org.fedoraproject.LangPack-km.metainfo.xml

%langcore_pkg -l km -n Khmer -f khmer-os-system-fonts

%package kn
Summary: Kannada langpacks meta-package
Requires: %{name}-core-kn
Recommends: google-noto-sans-kannada-vf-fonts
Recommends: google-noto-sans-kannada-ui-vf-fonts
Recommends: gubbi-fonts
Recommends: navilu-fonts

%description kn
This package provides Kannada langpacks meta-package.

%files kn
%{_datadir}/metainfo/org.fedoraproject.LangPack-kn.metainfo.xml

%langcore_pkg -l kn -n Kannada -f lohit-kannada-fonts -i ibus-m17n

%package ko
Summary: Korean langpacks meta-package
Requires: %{name}-core-ko
Recommends: google-noto-serif-cjk-ttc-fonts

%description ko
This package provides Korean langpacks meta-package.

%files ko
%{_datadir}/metainfo/org.fedoraproject.LangPack-ko.metainfo.xml

%langcore_pkg -l ko -n Korean -f google-noto-sans-cjk-ttc-fonts -i ibus-hangul

%package ku
Summary: Kurdish langpacks meta-package
Requires: %{name}-core-ku

%description ku
This package provides Kurdish langpacks meta-package.

%files ku
%{_datadir}/metainfo/org.fedoraproject.LangPack-ku.metainfo.xml

%langcore_pkg -l ku -n Kurdish

%package lt
Summary: Lithuanian langpacks meta-package
Requires: %{name}-core-lt

%description lt
This package provides Lithuanian langpacks meta-package.

%files lt
%{_datadir}/metainfo/org.fedoraproject.LangPack-lt.metainfo.xml

%langcore_pkg -l lt -n Lithuanian

%package lv
Summary: Latvian langpacks meta-package
Requires: %{name}-core-lv

%description lv
This package provides Latvian langpacks meta-package.

%files lv
%{_datadir}/metainfo/org.fedoraproject.LangPack-lv.metainfo.xml

%langcore_pkg -l lv -n Latvian

%package mai
Summary: Maithili langpacks meta-package
Requires: %{name}-core-mai
Recommends: google-noto-sans-devanagari-vf-fonts
Recommends: google-noto-sans-devanagari-ui-vf-fonts

%description mai
This package provides Maithili langpacks meta-package.

%files mai
%{_datadir}/metainfo/org.fedoraproject.LangPack-mai.metainfo.xml

%langcore_pkg -l mai -n Maithili -f lohit-devanagari-fonts -i ibus-m17n

%package mk
Summary: Macedonian langpacks meta-package
Requires: %{name}-core-mk

%description mk
This package provides Macedonian langpacks meta-package.

%files mk
%{_datadir}/metainfo/org.fedoraproject.LangPack-mk.metainfo.xml

%langcore_pkg -l mk -n Macedonian

%package ml
Summary: Malayalam langpacks meta-package
Requires: %{name}-core-ml
Recommends: google-noto-sans-malayalam-vf-fonts
Recommends: google-noto-sans-malayalam-ui-vf-fonts
Recommends: lohit-malayalam-fonts
Recommends: samyak-malayalam-fonts
Recommends: smc-anjalioldlipi-fonts
Recommends: smc-dyuthi-fonts
Recommends: smc-rachana-fonts
Recommends: smc-raghumalayalamsans-fonts
Recommends: smc-suruma-fonts

%description ml
This package provides Malayalam langpacks meta-package.

%files ml
%{_datadir}/metainfo/org.fedoraproject.LangPack-ml.metainfo.xml

%langcore_pkg -l ml -n Malayalam -f smc-meera-fonts -i ibus-m17n

%package mr
Summary: Marathi langpacks meta-package
Requires: %{name}-core-mr
Recommends: google-noto-sans-devanagari-vf-fonts
Recommends: google-noto-sans-devanagari-ui-vf-fonts
Recommends: samyak-devanagari-fonts

%description mr
This package provides Marathi langpacks meta-package.

%files mr
%{_datadir}/metainfo/org.fedoraproject.LangPack-mr.metainfo.xml

%langcore_pkg -l mr -n Marathi -f lohit-marathi-fonts -i ibus-m17n

%package ms
Summary: Malay langpacks meta-package
Requires: %{name}-core-ms

%description ms
This package provides Malay langpacks meta-package.

%files ms
%{_datadir}/metainfo/org.fedoraproject.LangPack-ms.metainfo.xml

%langcore_pkg -l ms -n Malay

%package my
Summary: Burmese langpacks meta-package
Requires: %{name}-core-my

%description my
This package provides Burmese langpacks meta-package.

%files my
%{_datadir}/metainfo/org.fedoraproject.LangPack-my.metainfo.xml

%langcore_pkg -l my -n Burmese -f sil-padauk-fonts

%package nb
Summary: Norwegian Bokmål langpacks meta-package
Requires: %{name}-core-nb

%description nb
This package provides Norwegian Bokmål langpacks meta-package.

%files nb
%{_datadir}/metainfo/org.fedoraproject.LangPack-nb.metainfo.xml

%langcore_pkg -l nb -n %{quote:Norwegian Bokmål}

%package ne
Summary: Nepali langpacks meta-package
Requires: %{name}-core-ne
Recommends: google-noto-sans-devanagari-vf-fonts
Recommends: google-noto-sans-devanagari-ui-vf-fonts

%description ne
This package provides Nepali langpacks meta-package.

%files ne
%{_datadir}/metainfo/org.fedoraproject.LangPack-ne.metainfo.xml

%langcore_pkg -l ne -n Nepali -f lohit-devanagari-fonts madan-fonts -i ibus-m17n

%package nl
Summary: Dutch langpacks meta-package
Requires: %{name}-core-nl

%description nl
This package provides Dutch langpacks meta-package.

%files nl
%{_datadir}/metainfo/org.fedoraproject.LangPack-nl.metainfo.xml

%langcore_pkg -l nl -n Dutch

%package nn
Summary: Nynorsk langpacks meta-package
Requires: %{name}-core-nn

%description nn
This package provides Nynorsk langpacks meta-package.

%files nn
%{_datadir}/metainfo/org.fedoraproject.LangPack-nn.metainfo.xml

%langcore_pkg -l nn -n Nynorsk

%package nr
Summary: Southern Ndebele langpacks meta-package
Requires: %{name}-core-nr

%description nr
This package provides Southern Ndebele langpacks meta-package.

%files nr
%{_datadir}/metainfo/org.fedoraproject.LangPack-nr.metainfo.xml

%langcore_pkg -l nr -n %{quote:Southern Ndebele}

%package nso
Summary: Northern Sotho langpacks meta-package
Requires: %{name}-core-nso

%description nso
This package provides Northern Sotho langpacks meta-package.

%files nso
%{_datadir}/metainfo/org.fedoraproject.LangPack-nso.metainfo.xml

%langcore_pkg -l nso -n %{quote:Northern Sotho}

%package or
Summary: Odia langpacks meta-package
Requires: %{name}-core-or
Recommends: samyak-odia-fonts

%description or
This package provides Odia langpacks meta-package.

%files or
%{_datadir}/metainfo/org.fedoraproject.LangPack-or.metainfo.xml

%langcore_pkg -l or -n Odia -f lohit-odia-fonts -i ibus-m17n

%package pa
Summary: Punjabi langpacks meta-package
Requires: %{name}-core-pa
Recommends: saab-fonts
Recommends: lohit-gurmukhi-fonts

%description pa
This package provides Punjabi langpacks meta-package.

%files pa
%{_datadir}/metainfo/org.fedoraproject.LangPack-pa.metainfo.xml

%langcore_pkg -l pa -n Punjabi -f google-noto-sans-gurmukhi-fonts -i ibus-m17n

%package pl
Summary: Polish langpacks meta-package
Requires: %{name}-core-pl

%description pl
This package provides Polish langpacks meta-package.

%files pl
%{_datadir}/metainfo/org.fedoraproject.LangPack-pl.metainfo.xml

%langcore_pkg -l pl -n Polish

%package pt_BR
Summary: Portuguese (Brazil) langpacks meta-package
Requires: %{name}-core-pt_BR

%description pt_BR
This package provides Portuguese (Brazil) langpacks meta-package.

%files pt_BR
%{_datadir}/metainfo/org.fedoraproject.LangPack-pt_BR.metainfo.xml

%langcore_pkg -l pt_BR -n %{quote:Portuguese (Brazil)}

%package pt
Summary: Portuguese langpacks meta-package
Requires: %{name}-core-pt

%description pt
This package provides Portuguese langpacks meta-package.

%files pt
%{_datadir}/metainfo/org.fedoraproject.LangPack-pt.metainfo.xml

%langcore_pkg -l pt -n Portuguese

%package ro
Summary: Romanian langpacks meta-package
Requires: %{name}-core-ro

%description ro
This package provides Romanian langpacks meta-package.

%files ro
%{_datadir}/metainfo/org.fedoraproject.LangPack-ro.metainfo.xml

%langcore_pkg -l ro -n Romanian

%package ru
Summary: Russian langpacks meta-package
Requires: %{name}-core-ru
Recommends: paratype-pt-sans-fonts

%description ru
This package provides Russian langpacks meta-package.

%files ru
%{_datadir}/metainfo/org.fedoraproject.LangPack-ru.metainfo.xml

%langcore_pkg -l ru -n Russian

%package si
Summary: Sinhala langpacks meta-package
Requires: %{name}-core-si

%description si
This package provides Sinhala langpacks meta-package.

%files si
%{_datadir}/metainfo/org.fedoraproject.LangPack-si.metainfo.xml

%langcore_pkg -l si -n Sinhala -f google-noto-sans-sinhala-vf-fonts -i ibus-sayura ibus-m17n

%package sk
Summary: Slovak langpacks meta-package
Requires: %{name}-core-sk

%description sk
This package provides Slovak langpacks meta-package.

%files sk
%{_datadir}/metainfo/org.fedoraproject.LangPack-sk.metainfo.xml

%langcore_pkg -l sk -n Slovak

%package sl
Summary: Slovenian langpacks meta-package
Requires: %{name}-core-sl

%description sl
This package provides Slovenian langpacks meta-package.

%files sl
%{_datadir}/metainfo/org.fedoraproject.LangPack-sl.metainfo.xml

%langcore_pkg -l sl -n Slovenian

%package sq
Summary: Albanian langpacks meta-package
Requires: %{name}-core-sq

%description sq
This package provides Albanian langpacks meta-package.

%files sq
%{_datadir}/metainfo/org.fedoraproject.LangPack-sq.metainfo.xml

%langcore_pkg -l sq -n Albanian

%package sr
Summary: Serbian langpacks meta-package
Requires: %{name}-core-sr

%description sr
This package provides Serbian langpacks meta-package.

%files sr
%{_datadir}/metainfo/org.fedoraproject.LangPack-sr.metainfo.xml

%langcore_pkg -l sr -n Serbian

%package ss
Summary: Swati langpacks meta-package
Requires: %{name}-core-ss

%description ss
This package provides Swati langpacks meta-package.

%files ss
%{_datadir}/metainfo/org.fedoraproject.LangPack-ss.metainfo.xml

%langcore_pkg -l ss -n Swati

%package sv
Summary: Swedish langpacks meta-package
Requires: %{name}-core-sv

%description sv
This package provides Swedish langpacks meta-package.

%files sv
%{_datadir}/metainfo/org.fedoraproject.LangPack-sv.metainfo.xml

%langcore_pkg -l sv -n Swedish

%package ta
Summary: Tamil langpacks meta-package
Requires: %{name}-core-ta
Recommends: google-noto-sans-tamil-vf-fonts
Recommends: google-noto-sans-tamil-ui-vf-fonts
Recommends: samyak-tamil-fonts
Recommends: serafettin-cartoon-fonts

%description ta
This package provides Tamil langpacks meta-package.

%files ta
%{_datadir}/metainfo/org.fedoraproject.LangPack-ta.metainfo.xml

%langcore_pkg -l ta -n Tamil -f lohit-tamil-fonts -i ibus-m17n

%package te
Summary: Telugu langpacks meta-package
Requires: %{name}-core-te
Recommends: google-noto-sans-telugu-fonts
Recommends: google-noto-sans-telugu-ui-fonts
Recommends: pothana2000-fonts
Recommends: vemana2000-fonts

%description te
This package provides Telugu langpacks meta-package.

%files te
%{_datadir}/metainfo/org.fedoraproject.LangPack-te.metainfo.xml

%langcore_pkg -l te -n Telugu -f lohit-telugu-fonts -i ibus-m17n

%package th
Summary: Thai langpacks meta-package
Requires: %{name}-core-th
Recommends: google-noto-sans-thai-vf-fonts
Recommends: google-noto-sans-thai-ui-vf-fonts
Recommends: google-noto-serif-thai-vf-fonts
Recommends: thai-scalable-garuda-fonts
Recommends: thai-scalable-kinnari-fonts
Recommends: thai-scalable-loma-fonts
Recommends: thai-scalable-norasi-fonts
Recommends: thai-scalable-purisa-fonts
Recommends: thai-scalable-sawasdee-fonts
Recommends: thai-scalable-tlwgmono-fonts
Recommends: thai-scalable-tlwgtypewriter-fonts
Recommends: thai-scalable-tlwgtypist-fonts
Recommends: thai-scalable-tlwgtypo-fonts
Recommends: thai-scalable-umpush-fonts

%description th
This package provides Thai langpacks meta-package.

%files th
%{_datadir}/metainfo/org.fedoraproject.LangPack-th.metainfo.xml

%langcore_pkg -l th -n Thai -f thai-scalable-waree-fonts -i ibus-m17n

%package tn
Summary: Tswana langpacks meta-package
Requires: %{name}-core-tn

%description tn
This package provides Tswana langpacks meta-package.

%files tn
%{_datadir}/metainfo/org.fedoraproject.LangPack-tn.metainfo.xml

%langcore_pkg -l tn -n Tswana

%package tr
Summary: Turkish langpacks meta-package
Requires: %{name}-core-tr

%description tr
This package provides Turkish langpacks meta-package.

%files tr
%{_datadir}/metainfo/org.fedoraproject.LangPack-tr.metainfo.xml

%langcore_pkg -l tr -n Turkish

%package ts
Summary: Tsonga langpacks meta-package
Requires: %{name}-core-ts

%description ts
This package provides Tsonga langpacks meta-package.

%files ts
%{_datadir}/metainfo/org.fedoraproject.LangPack-ts.metainfo.xml

%langcore_pkg -l ts -n Tsonga

%package uk
Summary: Ukrainian langpacks meta-package
Requires: %{name}-core-uk

%description uk
This package provides Ukrainian langpacks meta-package.

%files uk
%{_datadir}/metainfo/org.fedoraproject.LangPack-uk.metainfo.xml

%langcore_pkg -l uk -n Ukrainian

%package ur
Summary: Urdu langpacks meta-package
Requires: %{name}-core-ur
Recommends: dejavu-sans-fonts
Recommends: dejavu-sans-mono-fonts
Recommends: nafees-nastaleeq-fonts
Recommends: nafees-web-naskh-fonts

%description ur
This package provides Urdu langpacks meta-package.

%files ur
%{_datadir}/metainfo/org.fedoraproject.LangPack-ur.metainfo.xml

%langcore_pkg -l ur -n Urdu -f paktype-naskh-basic-fonts -i ibus-m17n

%package ve
Summary: Venda langpacks meta-package
Requires: %{name}-core-ve

%description ve
This package provides Venda langpacks meta-package.

%files ve
%{_datadir}/metainfo/org.fedoraproject.LangPack-ve.metainfo.xml

%langcore_pkg -l ve -n Venda

%package vi
Summary: Vietnamese langpacks meta-package
Requires: %{name}-core-vi

%description vi
This package provides Vietnamese langpacks meta-package.

%files vi
%{_datadir}/metainfo/org.fedoraproject.LangPack-vi.metainfo.xml

%langcore_pkg -l vi -n Vietnamese -i ibus-bogo

%package xh
Summary: Xhosa langpacks meta-package
Requires: %{name}-core-xh

%description xh
This package provides Xhosa langpacks meta-package.

%files xh
%{_datadir}/metainfo/org.fedoraproject.LangPack-xh.metainfo.xml

%langcore_pkg -l xh -n Xhosa

%package yi
Summary: Yiddish langpacks meta-package
Requires: %{name}-core-yi
Recommends: culmus-aharoni-clm-fonts
Recommends: culmus-caladings-clm-fonts
Recommends: culmus-david-clm-fonts
Recommends: culmus-drugulin-clm-fonts
Recommends: culmus-ellinia-clm-fonts
Recommends: culmus-frank-ruehl-clm-fonts
Recommends: culmus-hadasim-clm-fonts
Recommends: culmus-keteryg-fonts
Recommends: culmus-miriam-clm-fonts
Recommends: culmus-miriam-mono-clm-fonts
Recommends: culmus-nachlieli-clm-fonts
Recommends: culmus-simple-clm-fonts
Recommends: culmus-stamashkenaz-clm-fonts
Recommends: culmus-stamsefarad-clm-fonts
Recommends: culmus-yehuda-clm-fonts

%description yi
This package provides Yiddish langpacks meta-package.

%files yi
%{_datadir}/metainfo/org.fedoraproject.LangPack-yi.metainfo.xml

%langcore_pkg -l yi -n Yiddish

%package zh_CN
Summary: Simplified Chinese langpacks meta-package
Requires: %{name}-core-zh_CN
Recommends: google-noto-serif-cjk-ttc-fonts

%description zh_CN
This package provides Simplified Chinese langpacks meta-package.

%files zh_CN
%{_datadir}/metainfo/org.fedoraproject.LangPack-zh_CN.metainfo.xml

%langcore_pkg -l zh_CN -n %{quote:Simplified Chinese} -f google-noto-sans-cjk-ttc-fonts -i ibus-libpinyin

%package zh_TW
Summary: Traditional Chinese langpacks meta-package
Requires: %{name}-core-zh_TW
Recommends: google-noto-serif-cjk-ttc-fonts

%description zh_TW
This package provides Traditional Chinese langpacks meta-package.

%files zh_TW
%{_datadir}/metainfo/org.fedoraproject.LangPack-zh_TW.metainfo.xml

%langcore_pkg -l zh_TW -n %{quote:Traditional Chinese} -f google-noto-sans-cjk-ttc-fonts -i ibus-libzhuyin

%package zu
Summary: Zulu langpacks meta-package
Requires: %{name}-core-zu

%description zu
This package provides Zulu langpacks meta-package.

%files zu
%{_datadir}/metainfo/org.fedoraproject.LangPack-zu.metainfo.xml

%langcore_pkg -l zu -n Zulu

%prep
# nothing to prep

%build
# nothing to build


%install
# Explode the metainfo files into the subpackages so they get added to the
# distro-specific AppStream metadata
mkdir -p %{buildroot}/usr/share/metainfo
DESTDIR=%{buildroot} appstream-util split-appstream %{SOURCE0}
DESTDIR=%{buildroot} appstream-util split-appstream %{SOURCE1}
DESTDIR=%{buildroot} appstream-util split-appstream %{SOURCE2}

%changelog
* Wed Sep 16 2020 Parag Nemade <pnemade AT redhat DOT com> - 3.0-5
- Resolves: Fix broken dependency for langpacks-core-font-km (#1879141)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Akira TAGOH <tagoh@redhat.com> - 3.0-3
- Stop shipping core-font sub-packages in lowercase and keep same naming as others.

* Tue Feb  4 2020 Akira TAGOH <tagoh@redhat.com> - 3.0-2
- Revert font(familyname) dependency to fix some regressions.

* Wed Jan 22 2020 Parag Nemade <pnemade AT redhat DOT com> - 3.0-1
- Added AppStream metainfo files for -core and -core-font subpackages
- Use fontconfig API to normalize the langcode
  and sub-package core-font based on ortho (By Akira Tagoh)
- Use dependencies as font(familyname) instead of actual package names
- Added Provides: in langcore_pkg macro (#1792463)
- Added -core-font-xx subpackages

* Wed Sep 11 2019 Parag Nemade <pnemade AT redhat DOT com> - 2.0-7
- Fix typo (#1751242)

* Thu Aug 29 2019 Parag Nemade <pnemade AT redhat DOT com> - 2.0-6
- Fix the issue detected in rpmdeplint report

* Mon Aug 12 2019 Akira TAGOH <tagoh@redhat.com> - 2.0-5
- Replace non variable fonts to variable fonts. (#1739976)

* Mon Jul 29 2019 Parag Nemade <pnemade AT redhat DOT com> - 2.0-4
- Resolves:rh#1733929 - 'Requires:' to 'Recommends:' for additional fonts in base langpacks

* Fri Jul 26 2019 Parag Nemade <pnemade AT redhat DOT com> - 2.0-3
- Resolves:rh#1554988 - google-noto-sans-gurmkukhi-fonts default for Punjabi

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Parag Nemade <pnemade AT redhat DOT com> - 2.0-1
- Should have bumped the version to 2.0 in last build

* Mon Jul 22 2019 Parag Nemade <pnemade AT redhat DOT com> - 1.0-18
- Implement F31 Change (rh#1732123)
- Improve langname expansion macro from Jens Petersen
- macronize langpacks-core-* subpackages
- Correct the fonts entry for -core packages
- for now no Recommends: but Requires:

* Fri Apr 12 2019 Parag Nemade <pnemade AT redhat DOT com> - 1.0-17
- Resolves: rh#1699210 - langpack-pa: add "Recommends: google-noto-sans-gurmukhi-fonts"

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Parag Nemade <pnemade AT redhat DOT com> - 1.0-15
- Added few new subpackages for bo, dz, ka, km, ku, my, yi
- Added entry for above languages in org.fedoraproject.LangPacks.xml
- Enhance few langpacks to pull input-method packages
- Enhance few langpacks to pull font packages

* Thu Nov 08 2018 Parag Nemade <pnemade AT redhat DOT com> - 1.0-14
- Resolves:rh#1644736: Added eo (Esperanto) language

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Parag Nemade <pnemade AT redhat DOT com> - 1.0-11
- Added description in appdata metainfo files (rh#1538105)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 15 2016 Richard Hughes <richard@hughsie.com> - 1.0-8
- Use a specific AppStream component type of localization.

* Mon Feb 29 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0-7
- Resolves:rh#1312890: langpacks-en should be added

* Fri Feb 26 2016 Richard Hughes <richard@hughsie.com> - 1.0-6
- Explode the metainfo files into the subpackages so they get added to the
  distro-specific AppStream metadata.
- This allows us to add and remove languages in GNOME Software.

* Tue Feb 23 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0-5
- Resolves:rh#1310538: Added br ga he nn nr ss tn ts ve xh languages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0-3
- Removed %%files to disable langpacks.noarch package

* Tue Jan 26 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0-2
- Changed metapackage -> meta-package
- Added information about how we chose language list

* Thu Jan 21 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0-1
- Initial packaging

