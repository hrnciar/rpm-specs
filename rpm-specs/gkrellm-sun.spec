%global gkplugindir %{_libdir}/gkrellm2/plugins

Name:           gkrellm-sun
Version:        1.0.0
Release:        30%{?dist}
Summary:        Sun clock plugin for GKrellM
License:        GPLv2
URL:            http://gkrellsun.sourceforge.net/
Source0:        http://downloads.sf.net/gkrellsun/gkrellsun-%{version}.tar.gz
Source1:        gnome-%{name}.metainfo.xml
# Fix a bunch of compiler warnings
Patch0:         gkrellsun-1.0.0-fixes.patch
# Fix rhbz 1231394
Patch1:         gkrellsun-1.0.0-rhbz1231394.patch
Requires:       gkrellm >= 2.2.0
BuildRequires:  gcc
BuildRequires:  gkrellm-devel >= 2.2.0
BuildRequires:  libappstream-glib

%description
A sun clock plugin for GKrellM which can display the sun's setting time,
rising time, path and current location and so on.


%prep
%setup -q -n gkrellsun-%{version}
%patch0 -p1
%patch1 -p1


%build
make %{?_smp_mflags} FLAGS='%{optflags} -fPIC $(GTK_INCLUDE)' \
    LFLAGS='%{__global_ldflags} -shared'


%install
install -D -m 0755 src20/gkrellsun.so \
    %{buildroot}%{gkplugindir}/gkrellsun.so
install -p -D -m 644 %{SOURCE1} \
    %{buildroot}%{_datadir}/appdata/gnome-%{name}.metainfo.xml
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/appdata/gnome-%{name}.metainfo.xml


%files
%doc AUTHORS README
%license COPYING
%{gkplugindir}/gkrellsun.so
%{_datadir}/appdata/gnome-%{name}.metainfo.xml


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-30
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 27 2016 Hans de Goede <hdegoede@redhat.com> - 1.0.0-20
- Set LFLAGS, use global instead of define, use smp_flags (rhbz#1312561)

* Sat Feb 27 2016 Hans de Goede <hdegoede@redhat.com> - 1.0.0-19
- Clean-up specfile for unretire re-review of gkrellm-sun
- Fix crash after sun-plugin has been disabled (rhbz#1231394)
- Add appdata

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar  9 2012 Tom Callaway <spot@fedoraproject.org> - 1.0.0-12
- fix FTBFS
