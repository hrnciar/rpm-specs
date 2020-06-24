%global fontname        nafees-pakistani-naskh
%global fontconf        67-%{fontname}.conf
%global archivename     Nafees_Pakistani_Naskh_v2.01

Name:           %{fontname}-fonts
Version:        2.01
Release:        18%{?dist}
Summary:        Nafees pakistani naskh font for writing Urdu in the Naskh script

License:        Bitstream Vera
URL:            http://www.crulp.org/index.htm

Source0:        http://www.crulp.org/Downloads/localization/fonts/NafeesPakistaniNaskh/%{archivename}.zip

Source1:        %{fontname}-update-preferred-family.pe
Source2:        %{fontconf}
Source3:       %{fontname}.metainfo.xml

BuildArch:      noarch
Requires:       fontpackages-filesystem
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge

%description

The Nafees Pakistani Naskh Font is the extension of Nafees Naskh.\
Nafees Pakistani Naskh Font for writing Urdu, Balochi, Pashto, Punjabi, \
Sindhi and Saraiki in Naskh script.


%prep
%setup -q -c

%build
# Fix RHBZ#490830 while not fixed upstream
%{_bindir}/fontforge %{SOURCE1} Nafees\ Pakistani\ Naskh\ v2.01.ttf
rm  Nafees\ Pakistani\ Naskh\ v2.01.ttf

%install

#fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
                %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}


# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
       %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml


%_font_pkg -f %{fontconf} *.ttf

%doc  *.pdf
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 06 2014 Pravin Satpute <psatpute@redhat.com> - 2.01-9
- Added metainfo for gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Pravin Satpute <psatpute@redhat.com> 2.01-6
- Resolved build failure bug #914207

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 23 2011 Pravin Satpute <psatpute@redhat.com> 2.01-2
- Updated as per review comments

* Wed Aug 10 2011 Pravin Satpute <psatpute@redhat.com> 2.01-1
- Initial packaging
