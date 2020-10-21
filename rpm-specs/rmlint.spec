Name:           rmlint
Version:        2.10.1
Release:        3%{?dist}
Summary:        Finds space waste and other broken things on your filesystem
# GPLv3: main code
# MIT: metrohash
# BSD: xxHash Library
# CC0 or ASL 2.0 or OpenSSL: blake2
# Public code: MurmurHash3, sha3
License:        GPLv3 and MIT and BSD and (CC0 or ASL 2.0 or OpenSSL) and Public Domain
URL:            https://rmlint.rtfd.org
Source0:        https://github.com/sahib/rmlint/archive/v%{version}/%{name}-%{version}.tar.gz


BuildRequires:  scons
BuildRequires:  gcc
BuildRequires:  python3-sphinx
BuildRequires:  python3-devel
BuildRequires:  gettext
BuildRequires:  libblkid-devel
BuildRequires:  elfutils-libelf-devel
BuildRequires:  glib2-devel
BuildRequires:  sqlite-devel
BuildRequires:  json-glib-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

Provides:       bundled(blake2)
Provides:       bundled(sha3)
Provides:       bundled(xxhash)
Provides:       bundled(metrohash)
Provides:       bundled(murmurhash3)

%description
Rmlint finds space waste and other broken things and offers to remove it. It is
especially an extremely fast tool to remove duplicates from your filesystem.

%prep
%autosetup -p1
for f in `find gui/shredder -name "*.py"`; do
    sed '1{\@^#!/usr/bin/env python@d}' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
done

%build
%set_build_flags
scons config
scons %{?_smp_mflags} DEBUG=1 SYMBOLS=1 --prefix=%{buildroot}%{_prefix} --actual-prefix=%{_prefix} --libdir=%{_lib}

%install
scons install DEBUG=1 SYMBOLS=1 --prefix=%{buildroot}%{_prefix} --actual-prefix=%{_prefix} --libdir=%{_lib}.
desktop-file-validate %{buildroot}/%{_datadir}/applications/shredder.desktop
%find_lang %{name}

%files -f %{name}.lang
%doc README.rst
%license COPYING
%{_bindir}/rmlint
%{_datadir}/applications/shredder.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Shredder.gschema.xml
%exclude %{_datadir}/glib-2.0/schemas/gschemas.compiled
%{_datadir}/icons/hicolor/scalable/apps/shredder.svg
%{_mandir}/man1/rmlint.1*
%{python3_sitelib}/shredder/
%{python3_sitelib}/Shredder-%{version}.*-py*.egg-info

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 16:03:30 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.10.1-1
- Update to 2.10.1 (#1842300)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-4
- Rebuilt for Python 3.9

* Sun Feb 02 18:32:39 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.9.0-3
- Fix FTBFS with GCC 10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.9.0-1
- Release 2.9.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Dec 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.8.0-1
- Update version to 2.8.0

* Sun May 10 2015 Christopher Pahl <sahib@online.de> - 2.2.0-1
- Update version to 2.2.0

* Sun Jan 12 2015 Christopher Pahl <sahib@online.de> - 2.0.0-4
- Fix rpm for lib separation.

* Sat Dec 20 2014 Christopher Pahl <sahib@online.de> - 2.0.0-3
- Use autosetup instead of setup -q

* Fri Dec 19 2014 Christopher Pahl <sahib@online.de> - 2.0.0-2
- Updated wrong dependency list

* Mon Dec 01 2014 Christopher Pahl <sahib@online.de> - 2.0.0-1
- Initial release of RPM package
