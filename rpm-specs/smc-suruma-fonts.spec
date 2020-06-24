%global fontname smc-suruma
%global fontconf 67-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	3.2.3
Release:	1%{?dist}
Epoch:		1
Summary:	Open Type Fonts for Malayalam script 
License:	GPLv3+ with exceptions
URL:		https://gitlab.com/smc/fonts/suruma
Source0:	%{url}/-/archive/Version%{version}/suruma-Version%{version}.tar.gz
Source1:	%{fontname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
BuildRequires:	fontforge
Requires:	fontpackages-filesystem
Obsoletes:	smc-fonts-common < 6.1-11

%description
Suruma-3.2.1 is a rehash of earlier releases. 
The earlier idea of akhand conjuncts for *RA *LA forms is revisited and 
implemented again with the new opentype specs. The new specs do away 
with statically-assigned character properties (by the shaping engine) 
for consonants. Instead, they are font dependent. i.e., post-base forms,
below-base forms etc. are all decided by the the font itself. 
This concept was also used in the initial version of suruma font.

%prep
%autosetup -n suruma-Version%{version}

%build
make

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

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
%doc README
%license COPYING
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
* Mon Feb 17 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 1:3.2.3-1
- New release smc-suruma-fonts-3.2.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:3.2.2-2
- Font CI test added

* Mon Feb 25 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:3.2.2-1
- Build font from sources

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:3.2.1-2
- Update incorrect license and removed unwanted requires entry

* Wed Nov 28 2018 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:3.2.1-1
- first release of smc-suruma fonts
