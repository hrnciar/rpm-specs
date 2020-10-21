%global fontname unifrakturmaguntia
%global fontconf 61-%{fontname}-fonts.conf
%global source_date 20140706


Name:          %{fontname}-fonts
Version:       0
Release:       0.12.%{source_date}%{?dist}
Summary:       Font that provide a Fraktur typeface that may be embedded on websites
License:       OFL
URL:           http://unifraktur.sourceforge.net/maguntia.html
Source0:       http://sourceforge.net/projects/unifraktur/files/fonts/UnifrakturMaguntia.2014-07-06.zip
Source10:      %{fontconf}
BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: fontforge
Requires:      fontpackages-filesystem

%description
UnifrakturMaguntia is based on Peter Wiegel’s font Berthold Mainzer Fraktur. The
main differences from Peter Wiegel’s font are the following:

- UnifrakturMaguntia uses OpenType for displaying the font’s ligatures.
- UnifrakturMaguntia is suitable for @font-face embedding on the internet. It
  has a permissive license, the OFL, that explicitly allows font embedding.
- G. Ansmann has carefully redrawn all glyphs and significantly expanded the
  font.


%prep
%setup -q -n UnifrakturMaguntia.2014-07-06
# Correct end of line encoding for OFL.txt
sed -i 's/\r$//' OFL.txt


%build
fontforge -lang=ff -script "-" *.sfdir <<_EOF
i = 1
while ( i < \$argc )
  Open (\$argv[i], 1)
  Generate (\$fontname + ".ttf")
  PrintSetup (5)
  PrintFont (0, 0, "", \$fontname + "-sample.pdf")
  Close()
  i++
endloop
_EOF

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} \
    %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.ttf
%doc OFL.txt *.pdf


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20140706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20140706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20140706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20140706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20140706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20140706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20140706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20140706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20140706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20140706
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 17 2014 Julien Enselme <jujens@jujens.eu> - 0-0.2.20140706
- Correct the url of Source0.
- Correct Summary.
- Remove unuseful command in prep section.
- Fix version.

* Tue Sep 16 2014 Julien Enselme <jujens@jujens.eu> - 2014-0.1.20140706
- Initial packaging.
