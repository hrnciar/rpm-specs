Name:           minetestmapper
Version:        20200328
Release:        1%{?dist}
Summary:        Generates a overview image of a minetest map

License:        BSD
URL:            https://github.com/minetest/minetestmapper
Source0:        https://github.com/minetest/minetestmapper/archive/%{version}/minetestmapper-%{version}.tar.gz

BuildRequires:  gcc-c++, cmake, sqlite-devel, gd-devel, leveldb-devel, hiredis-devel, libpq-devel

# Wants minetest for ownership of /usr/share/minetest.
# But there's no reason it should *require* minetest.
Suggests:       minetest

%description
Generates a overview image of a minetest map. This is a port of
minetestmapper.py to C++, that is both faster and provides more
details than the deprecated Python script.

%prep
%autosetup -p1

# https://github.com/minetest/minetestmapper/issues/57
sed 's/get_setting/read_setting/g' -i db-postgresql.cpp

%build
%cmake -DENABLE_LEVELDB=1 -DENABLE_REDIS=1 -DENABLE_POSTGRESQL=1 .
%make_build

%install
%make_install

# Install colors.txt into /usr/share/minetest.
mkdir -p %{buildroot}%{_datadir}/minetest
cp -a colors.txt %{buildroot}%{_datadir}/minetest/

# Remove copy of license from docdir.
rm -rf %{buildroot}%{_pkgdocdir}/COPYING

%files
%{_bindir}/minetestmapper
%{_datadir}/minetest/
%{_datadir}/minetest/colors.txt
%{_mandir}/man6/minetestmapper.6*
%license COPYING
%doc AUTHORS README.rst

%changelog
* Tue Apr 21 2020 Ben Rosser <rosser.bjr@gmail.com> - 20200328-1
- Update to latest upstream release (rhbz#1818531).

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20191011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 20191011-1
- 2019-10-11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180325-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180325-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 20180325-3
- Append curdir to CMake invokation. (#1668512)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180325-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Ben Rosser <rosser.bjr@gmail.com> - 20180325-1
- Updated to latest upstream release (rhbz#1560540).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170606-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 06 2017 Ben Rosser <rosser.bjr@gmail.com> - 20170606-5
- Instead of requiring minetest, only suggest it.
- Have minetestmapper also own the datadir/minetest directory.

* Thu Aug 24 2017 Ben Rosser <rosser.bjr@gmail.com> - 20170606-4
- Add ExcludeArch to s390x due to the lack of minetest.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170606-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170606-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Ben Rosser <rosser.bjr@gmail.com> - 20170606-1
- Update to latest upstream release.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161218-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Ben Rosser <rosser.bjr@gmail.com> - 20161218-3
- Add ExcludeArch on ppc arches due to lack of minetest on them

* Fri Jan 20 2017 Ben Rosser <rosser.bjr@gmail.com> - 20161218-2
- Add man page for minetestmapper written by dmoerner.
- Reference patches without using a URL.
- Use version macro in Source0 URL.

* Fri Jan  6 2017 Ben Rosser <rosser.bjr@gmail.com> - 20161218-1
- Initial package for Fedora.
