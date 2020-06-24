%global fontname smc-meera
%global fontconf 65-0-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	7.0.3
Release:	1%{?dist}
Summary:	Open Type Fonts for Malayalam script
License:	OFL
URL:		https://gitlab.com/smc/fonts/meera
Source0:	%{url}/-/archive/Version%{version}/meera-Version%{version}.tar.gz
Source1:	%{fontname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
BuildRequires:	fontforge-devel
BuildRequires:	python3
BuildRequires:	python3-fonttools
Requires:	fontpackages-filesystem
Obsoletes:	smc-fonts-common < 6.1-11

%description
Meera font is a Malayalam font designed by Hussain K H and 
maintained by Swathanthra Malayalam Computing project. This 
is a comprehensive Malayalam font with 1000+ glyphs for all 
common Malayalam ligatures.

%prep
%autosetup -n meera-Version%{version}
chmod 644 *.txt
rm -rf ttf

%build 
make PY=python3

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p build/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

install -Dm 0644 -p %{SOURCE2} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

ln -s %{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}

%check
appstream-util validate-relax --nonet \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc README.md
%license LICENSE.txt
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
* Mon Feb 17 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 7.0.3-1
- New release smc-meera-fonts-7.0.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 7.0.1-4
- Font CI test added

* Mon Feb 25 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 7.0.1-3
- Build font from sources

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 7.0.1-1
- first release of smc-meera fonts
