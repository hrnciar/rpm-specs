%global fontname grimmer-proggy-squaresz
%global fontconf 66-%{fontname}.conf

Name: %{fontname}-fonts
Version: 1.0
Release: 7%{?dist}
License: MIT
URL: http://upperbounds.net/
Source0: http://upperbounds.net/download/ProggySquareSZ.ttf.zip
Source1: 66-grimmer-proggy-squaresz.conf
Source2: %{fontname}.metainfo.xml

BuildArch: noarch
Summary: Proggy Square with slashed zero programming font
BuildRequires: fontpackages-devel
BuildRequires: libappstream-glib
Requires: fontpackages-filesystem

%description
The proggy fonts are a set of fixed-width screen fonts that are designed for
code listings. Proggy Square Slashed Zero is identical to Proggy Square but
has a slashed zero instead of a dot.

%prep
%setup -q -c -n %{name}-%{version}

%build
sed -i 's/\r//' Licence.txt

%install
mkdir -p %{buildroot}/%{_fontdir}

install -m 0644 ProggySquareSZ.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

appstream-util validate-relax --nonet \
               %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc Licence.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Bojan Smojver <bojan@rexursive.com> - 1.0-2
- incorporate fixes for errors found in package review

* Tue May 23 2017 Bojan Smojver <bojan@rexursive.com> - 1.0-1
- initial packaging
