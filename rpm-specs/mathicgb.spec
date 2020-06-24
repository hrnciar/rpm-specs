%global gitdate         20181123
%global gittag          636952f94bf6bb6d82a84f0c9ac7f44373f8a34f
%global shorttag        %(c=%{gittag}; echo ${c:0:7})
%global user            Macaulay2

Name:           mathicgb
Version:        1.0
Release:        19.%{gitdate}.git%{shorttag}%{?dist}
Summary:        Groebner basis computations

License:        GPLv2+
URL:            https://github.com/%{user}/%{name}
Source0:        https://github.com/%{user}/%{name}/tarball/%{gittag}/%{user}-%{name}-%{shorttag}.tar.gz
# The tests are incompatible with gtest-1.8.0+, so do this instead
Source1:        https://github.com/google/googletest/archive/release-1.6.0.tar.gz
# Fix build failure on big endian machines.
# See https://github.com/Macaulay2/mathicgb/issues/3
Patch0:         %{name}-endian.patch

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  mathic-devel
BuildRequires:  tbb-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Mathicgb is a program for computing Groebner basis and signature Grobner
bases.  Mathicgb is based on the fast data structures from mathic.

%package devel
Summary:        Development files for mathicgb
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Files for developing applications that use mathicgb.

%package libs
Summary:        Mathicgb libraries

%description libs
Library interface to mathicgb.

%prep
%autosetup -p0 -n %{user}-%{name}-%{shorttag}

# Unpack gtest
rm -fr libs
tar xzf %{SOURCE1}
mv googletest-release-1.6.0 libs

# Fix end-of-line encoding
sed -i.orig 's/\r//' doc/description.txt
touch -r doc/description.txt.orig doc/description.txt
rm -f doc/description.txt.orig

# Nearly every file is marked executable; only a few need to be.
find . -type f -perm /0111 | xargs chmod a-x
chmod a+x autogen.sh fixspace replace build/setup/make-Makefile.sh

# Upstream doesn't generate the configure script
autoreconf -fi

%build
export CFLAGS="%{optflags} -fwrapv"
export CXXFLAGS="%{optflags} -fwrapv"
%configure --disable-static --enable-shared --with-gtest

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool
sed -i 's|g++$|& -Wl,--as-needed|' Makefile

make %{?_smp_mflags}

%install
%make_install

# We don't want the libtool archive
rm -f %{buildroot}%{_libdir}/lib%{name}.la

%check
export LD_LIBRARY_PATH=$PWD/.libs
make check

%ldconfig_scriptlets libs

%files
%doc README.md doc/description.txt doc/slides.pdf
%{_bindir}/mgb
%{_mandir}/man1/mgb.1*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%{_libdir}/lib%{name}.so.*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19.20181123.git636952f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18.20181123.git636952f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17.20181123.git636952f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Jerry James <loganjerry@gmail.com> - 1.0-16.20181123.git636952f
- Update to latest upstream snapshot

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 1.0-15.20170606.gitbd634c8
- Rebuild for tbb 2019_U1
- Bundle gtest 1.6.0 to avoid incompatibility with gtest 1.8.0+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14.20170606.gitbd634c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13.20170606.gitbd634c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 16 2017 Jerry James <loganjerry@gmail.com> - 1.0-12-20170606.gitbd634c8
- Remove mgb dependency on gtest

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 1.0-11.20170606.gitbd634c8
- Update to latest upstream snapshot

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10.20170104.git068ed9d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9.20170104.git068ed9d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8.20170104.git068ed9d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Feb 22 2017 Jerry James <loganjerry@gmail.com> - 1.0-7.20170104.git068ed9d
- Update to latest upstream snapshot
- Add -endian patch to fix build failure on big endian architectures

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7.20160202.gitbb268df
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Jerry James <loganjerry@gmail.com> - 1.0-6.20160202.gitbb268df
- Rebuild for tbb 2017

* Mon Apr  4 2016 Jerry James <loganjerry@gmail.com> - 1.0-5.20160202.gitbb268df
- Update to latest upstream snapshot

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4.20150903.git427e61f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jerry James <loganjerry@gmail.com> - 1.0-3.20150903.git427e61f
- Change to Macaulay2 repo
- Reenable TBB support now that the i386 bug has been fixed
- Use a patch instead of sed for gtest manipulations (mathicgb-gtest.patch)

* Tue Dec  1 2015 Jerry James <loganjerry@gmail.com> - 1.0-2.20131006.gitc72c945
- Do not use TBB for now

* Tue Dec  1 2015 Jerry James <loganjerry@gmail.com> - 1.0-1.20131006.gitc72c945
- Initial RPM
