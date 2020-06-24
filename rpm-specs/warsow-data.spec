Name:           warsow-data
Version:        2.1.2
Release:        5%{?dist}
Summary:        Game data for Warsow

# For a breakdown of the licensing, see license.txt
License:        CC-BY-SA and CC-BY-ND
URL:            https://www.warsow.net/
Source0:        http://sebastian.network/warsow/warsow-%{version}.tar.gz

BuildArch:      noarch

# Warsow is only ported to these architectures
%if 0%{?rhel} == 7
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

BuildRequires:  /usr/bin/dos2unix
Requires:       warsow = %{version}

%description
Warsow is a fast paced first person shooter consisting of cel-shaded
cartoon-like graphics with dark, flashy and dirty textures. Warsow is based on
the E-novel "Chasseur de bots" ("Bots hunter" in English) by Fabrice Demurger.
Warsow's codebase is built upon Qfusion, an advanced modification of the Quake
II engine.

This package installs the game data files (textures, maps, sounds, etc.).

%prep
%setup -q -n warsow-%{version}

# Convert to utf-8 and Unix line breaks
dos2unix docs/license.txt

# Remove executable permissions from data files
chmod 644 docs/*
find basewsw -type f | xargs chmod 644

%build
# nothing to build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/warsow
cp -a basewsw $RPM_BUILD_ROOT%{_datadir}/warsow/

%files
%license docs/license.txt
%{_datadir}/warsow/

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 04 2018 Kalev Lember <klember@redhat.com> - 2.1.2-1
- Update to 2.1.2
- Remove executable permissions from data files
- Update URL

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Pete Walter <pwalter@fedoraproject.org> - 2.1-3
- Don't put noarch in ExclusiveArch (#1298668)

* Wed Feb 01 2017 Pete Walter <pwalter@fedoraproject.org> - 2.1-2
- Add ExclusiveArch

* Wed Jun 08 2016 Pete Walter <pwalter@fedoraproject.org> - 2.1-1
- Initial Fedora package
