%define fontname sil-gentium-basic
%define fontconf 59-%{fontname}

%define common_desc \
Gentium Basic and Gentium Book Basic are font families based on the\
original Gentium design, but with additional weights. Both families come \
with a complete regular, bold, italic and bold italic set of fonts. \
These "Basic" fonts support only the Basic Latin and Latin-1 Supplement \
Unicode ranges, plus a selection of the more commonly used extended Latin\
characters, with miscellaneous diacritical marks, symbols and punctuation.


Name: %{fontname}-fonts
Version: 1.1
Release: 21%{?dist}
Summary: SIL Gentium Basic font family

License:   OFL
URL:       http://scripts.sil.org/Gentium_Basic
Source0:   GentiumBasic_110.zip
Source1:   %{fontname}-fontconfig.conf
Source2:   %{fontname}-book-fontconfig.conf
Source3:   %{fontname}.metainfo.xml
Source4:   %{fontname}-book.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel

Requires: %{name}-common = %{version}-%{release}

%description
%common_desc

This is the base variant.

%_font_pkg -f %{fontconf}.conf GenBas*.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%package common
Summary:  Common files of %{fontname}
Requires: fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{fontname} packages.

%package  -n %{fontname}-book-fonts
Summary:  SIL Gentium Book Basic font family
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-book-fonts
%common_desc

The "Book" family is slightly heavier.

%_font_pkg -n book -f %{fontconf}-book.conf GenBkBas*.ttf
%{_datadir}/appdata/%{fontname}-book.metainfo.xml


%prep
%setup -q -n "Gentium Basic 1.1"
for txt in *.txt ; do
        fold -s $txt > $txt.new
        sed -i 's/\r//' $txt.new
        touch -r $txt $txt.new
        mv $txt.new $txt
done

# Convert to UTF-8
iconv -f iso-8859-1 -t utf-8 GENTIUM-FAQ.txt -o GENTIUM-FAQ.txt_
touch -r GENTIUM-FAQ.txt GENTIUM-FAQ.txt_
mv GENTIUM-FAQ.txt_ GENTIUM-FAQ.txt

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}


install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

install -m 0644 -p %{SOURCE2} \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-book.conf

for fconf in %{fontconf}.conf\
         %{fontconf}-book.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-book.metainfo.xml


%files common
%doc FONTLOG.txt GENTIUM-FAQ.txt OFL-FAQ.txt OFL.txt


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 21 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.1-12
- Add metainfo file to show this font in gnome-software
- Remove duplicate dir %%{_fontdir}
- Clean the spec to follow current packaging guidelines

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Michael J Gruber <mjg@fedoraproject.org> - 1.1-7
- spec file clean up.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 <b.rahul.pm@gmail.com> - 1.1-3.fc11
- Changed the naming for srpm.

* Wed Jan 28 2009 <b.rahul.pm@gmail.com> - 1.1-2.fc11
- Changes according to package naming guidelines post-1.13  fontpackages.

* Tue Jan 06 2009 <b.rahul.pm@gmail.com> - 1.1-1.fc11
- Following new packaging guidelines.
