Name: vmod-uuid
Summary: UUID module for Varnish Cache
Version: 1.6
Release: 8%{?dist}
License: BSD
URL: https://github.com/otto-de/libvmod-uuid
Source0: https://github.com/otto-de/lib%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires: varnish%{?_isa} = %(pkg-config --silence-errors --modversion varnishapi || echo 0)
Requires: uuid

BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: uuid-devel
BuildRequires: varnish-devel
BuildRequires: varnish
BuildRequires: check-devel

# To build from a git checkout, add these
BuildRequires: automake
BuildRequires: libtool
BuildRequires: python3-docutils
BuildRequires: autoconf-archive

%description
UUID Varnish vmod used to generate a uuid, including versions 1, 3, 4 and 5
as specified in RFC 4122. See the RFC for details about the various versions.


%prep
%autosetup -n lib%{name}-%{version}


%build
./autogen.sh
%configure \
  --docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

# We have to remove rpath - not allowed in Fedora
# (This problem only visible on 64 bit arches)
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g;
        s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%check
%make_build check


%install
%make_install

# None of these for fedora/epel
find %{buildroot}/%{_libdir}/ -name '*.la' -delete
find %{buildroot}/%{_libdir}/ -name  '*.a' -delete


%files
%{_libdir}/varnish*/vmods/
%license LICENSE
%doc README.rst COPYING
%{_mandir}/man3/*.3*


%changelog
* Thu Mar 26 2020 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6-8
- Rebuilt against varnish-6.4.0

* Thu Mar 26 2020 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6-7
- Rebuilt against varnish-6.3.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6-5
- Rebuilt against varnish-6.3.1

* Wed Sep 25 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6-4
- Rebuilt against varnish-6.3.0-2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6-2
- Source tarball has no prebuilt manpages, so buildrequires python3-docutils
  for rst2man
- Now run make check in parallel

* Fri Feb 15 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.6-1
- New upstream release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5-3
- Rebuilt against varnish-6.1.1

* Thu Oct 11 2018 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5-2
- Rebuilt against varnish-6.0.1

* Tue Aug 07 2018 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5-1
- New upstream release
- Removed patch merged upstream

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.3-4
- Patched away obsolete m4 macro

* Fri Dec 08 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.3-3
- Added pkg-config call to compute correct varnish version dependency
- Removed el6 hacks from fedora candidate package
- Simplified and cleaned up macro usage and other cosmetics according to
  package review
- Added COPYING to doc

* Mon Nov 06 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.3-2
- Set a readable homepage URL
- Removed Group and BuildRoot tags
- Set _isa macro on varnish requirement
- Use license macro on all builds
- Build fixes for el6 added, though commented out (requires a dist tarball)

* Fri Nov 03 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.3-1
- New upstream release 1.3 aka ec75ddd

