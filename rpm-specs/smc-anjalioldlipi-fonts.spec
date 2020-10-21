%global fontname smc-anjalioldlipi
%global fontconf 67-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	7.1.2
Release:	2%{?dist}
Summary:	Open Type Fonts for Malayalam script 
License:	OFL
URL:		https://gitlab.com/smc/fonts/anjalioldlipi
Source0:	%{url}/-/archive/Version%{version}/anjalioldlipi-Version%{version}.tar.gz
Source1:	%{fontname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
BuildRequires:	brotli-devel
BuildRequires:	fontforge-devel
BuildRequires:	python3
BuildRequires:	python3-fonttools
Requires:	fontpackages-filesystem
Obsoletes:	smc-fonts-common < 6.1-11


%description
AnjaliOldLipi is a sans serif Malayalam language typeface designed
by Kevin & Siji and maintained by Swathanthra Malayalam Computing project.
This is a comprehensive font with glyphs for all common 
Malayalam ligatures and the Latin character set.

%prep
%autosetup -n anjalioldlipi-Version%{version}
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 7.1.2-1
- New release smc-anjalioldlipi-fonts-7.1.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 7.1.1-4
- Font CI test added

* Mon Feb 25 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 7.1.1-3
- Build font from sources

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 7.1.1-1
- first release of smc-anjalioldlipi fonts

