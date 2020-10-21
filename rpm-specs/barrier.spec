%global icon_path %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
Summary: Use a single keyboard and mouse to control multiple computers
Name: barrier
Version: 2.3.2
Release: 4%{?dist}
License: GPLv2
URL: https://github.com/debauchee/barrier/wiki
Source0: https://github.com/debauchee/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: cmake3
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libX11-devel
BuildRequires: libXtst-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: qt5-qtbase-devel

Requires: hicolor-icon-theme

%description
Barrier is software that mimics the functionality of a KVM switch, which
historically would allow you to use a single keyboard and mouse to control
multiple computers. Barrier does this in software, allowing you to tell it
which machine to control by moving your mouse to the edge of the screen,
or by using a key press to switch focus to a different system.

%prep
%setup -q

%build
mkdir build
cd build
%{cmake3} ..
%make_build
cd -

%install
cd build
install -D -p -m 0755 bin/barrier      %{buildroot}%{_bindir}/barrier
install -D -p -m 0755 bin/barrierc     %{buildroot}%{_bindir}/barrierc
install -D -p -m 0755 bin/barriers     %{buildroot}%{_bindir}/barriers
cd -
install -D -p -m 0644 res/barrier.desktop %{buildroot}%{_datadir}/applications/barrier.desktop
install -D -p -m 0644 doc/barrierc.1 %{buildroot}%{_mandir}/man1/barrierc.1
install -D -p -m 0644 doc/barriers.1 %{buildroot}%{_mandir}/man1/barriers.1
install -D -p -m 0644 res/barrier.ico  %{buildroot}%{_datadir}/pixmaps/barrier.ico
install -D -p -m 0644 res/barrier.svg %{buildroot}%{icon_path}
 
cd %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/metainfo
## Write AppStream
cat <<END> %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2020 Ding-Yi Chen <dchen@redhat.com> -->
<component type="desktop-application">
  <id>%{name}</id>
  <metadata_license>FSFAP</metadata_license>
  <project_license>GPLv2</project_license>
  <name>barrier</name>
  <summary>Use a single keyboard and mouse to control multiple computers</summary>

  <description>
    <p>
    Barrier is software that mimics the functionality of a KVM switch, which
    historically would allow you to use a single keyboard and mouse to control
    multiple computers. Barrier does this in software, allowing you to tell it
    which machine to control by moving your mouse to the edge of the screen,
    or by using a key press to switch focus to a different system.
    </p>
  </description>

  <launchable type="desktop-id">%{name}.desktop</launchable>

  <url type="homepage">%{url}</url>

  <provides>
    <binary>barrier</binary>
    <binary>barrierc</binary>
    <binary>barriers</binary>
  </provides>

  <releases>
    <release version="%{version}" date="2020-06-30" />
  </releases>
</component>
END

desktop-file-install --delete-original  \
  --dir %{buildroot}%{_datadir}/applications            \
  --set-icon=%{icon_path}           \
  %{buildroot}%{_datadir}/applications/barrier.desktop

desktop-file-validate %{buildroot}/%{_datadir}/applications/barrier.desktop

%files
# None of the documentation files are actually useful here, they all point to
# the online website, so include just one, the README
%license LICENSE
%doc ChangeLog res/Readme.txt doc/barrier.conf.example*
%{_bindir}/barrierc
%{_bindir}/barriers
%{_bindir}/barrier
%{_datadir}/pixmaps/barrier.ico
%{icon_path}
%{_datadir}/applications/barrier.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/barrierc.1*
%{_mandir}/man1/barriers.1*

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Ding-Yi Chen <dchen@redhat.com> -  2.3.2-2
- Address review comments:
  + Use better URL
  + BuildRequires added: gcc-c++
  + Requires add: hicolor-icon-theme
- BuildRequires remove: qt-devel


* Tue Jun 30 2020 Ding-Yi Chen <dchen@redhat.com> -  2.3.2-1
- Upstream update to 2.3.2
- Remove the link to synergy command to avoid package collision.

* Wed Jan 23 2019 Brian J. Murrell <brian@interlinx.bc.ca> - 2.1.2-1
- Initial RPM release, based on the spec from Fedora's synergy.
- Create convenience symlinks to old synergy* names for the benefit
  of tools that will have those names hard-coded, such as quicksynergy
