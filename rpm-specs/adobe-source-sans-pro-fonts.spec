%global fontname source-sans-pro
%global fontconf 63-%{fontname}.conf

Name:           adobe-source-sans-pro-fonts
Version:        3.006
Release:        2%{?dist}
Summary:        A set of OpenType fonts designed for user interfaces

License:        OFL
URL:            https://github.com/adobe-fonts/%{fontname}/
# Can't build fonts without nonfree softwares
Source0:        %{url}/releases/download/%{version}R/%{fontname}-%{version}R.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
BuildArch:      noarch

%description
Source Sans is a set of OpenType fonts that have been designed to work well in
user interface (UI) environments, as well as in text setting for screen and
print.


%prep
%autosetup -n %{fontname}-%{version}R


%build


%install
install -dm 0755 $RPM_BUILD_ROOT%{_fontdir}
install -pm 0644 OTF/*.otf $RPM_BUILD_ROOT%{_fontdir}

install -dm 0755 $RPM_BUILD_ROOT%{_fontconfig_templatedir} $RPM_BUILD_ROOT%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} $RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dpm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/appdata/%{fontname}.metainfo.xml


%_font_pkg -f %{fontconf} *.otf
%doc README.md
%license LICENSE.md
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.006-1
- Update to 3.006

* Fri Aug 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.045-1
- Update to 2.0.45

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.020-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.020-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.020-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 17 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.020-1
- Update to 2.020
- Update upstream URL
- Comply with latest packaging guidelines

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.050-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.050-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.050-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.050-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Richard Hughes <richard@hughsie.com> - 1.050-4
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.050-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.050-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Alexis Lameire <alexisis-pristontale@hotmail.com> - 1.050-1
- update to 1.050-1 upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.034-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 29 2012 Alexis Lameire <alexisis-pristontale@hotmail.com> - 1.034-1
- update to 1.034-1 upstream release

* Wed Aug 15 2012 Alexis Lameire <alexisis-pristontale@hotmail.com> - 1.033-3
- Drop useless doc file Readme.html

* Sat Aug 04 2012 Alexis Lameire <alexisis-pristontale@hotmail.com> - 1.033-2
- use versionned source

* Fri Aug 03 2012 Alexis Lameire <alexisis-pristontale@hotmail.com> - 1.033-1
- initial release

