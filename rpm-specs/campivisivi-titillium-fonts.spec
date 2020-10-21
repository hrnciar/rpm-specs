%global fontname campivisivi-titillium
%global fontconf 61-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	20120913
Release:	20%{?dist}
Summary:	Sans-serif typeface designed inside Campi Visivi's Type Design course

License:	OFL
URL:		http://www.campivisivi.net/titillium/
Source0:	http://www.campivisivi.net/titillium/download/Titillium_roman_upright_italic_2_0_OT.zip
Source1:	%{name}-fontconfig.conf
Source2:	%{name}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
Requires:	fontpackages-filesystem

%description
Sans-serif typeface from the Master of Visual Design Campi Visivi.

%prep
%setup -q -n "Titillium_roman_upright_italic_2_0_OT"

for file in *.txt; do
 sed 's/\r//g' "$file" | \
 fold -s > "$file.new" && \
 touch -r "$file" "$file.new" && \
 mv "$file.new" "$file"
done

%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
		%{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf

%{_datadir}/appdata/%{name}.metainfo.xml
%doc OFL-FAQ.txt OFL-titillium.txt


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 16 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 20130913-12
- Bump

* Wed Mar 16 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 20130913-11
- Reverted name of metainfo file

* Wed Mar 16 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 20120913-10
- Updated metainfo to adhere to appstream guideline
- Fixed typo within metainfo file
- Bumped for rebuild (release 8 and 9)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20120913-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120913-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Richard Hughes <richard@hughsie.com> - 20120913-5
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120913-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120913-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Luya Tshimbalanga <luya@fedoraproject.org> - 20120913-2
- Update spec based on fedora packaging review

* Mon Jul 22 2013 Luya Tshimbalanga <luya@fedoraproject.org> - 20120913-1
- Initial release
