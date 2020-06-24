# There have been no releases, so we use a git snapshot
%global gitdate         20160311
%global gittag          e85453b5bded99ffeccb645f8d400e989c970753
%global shorttag        %(cut -b -7 <<< %{gittag})
%global user            Macaulay2

Name:           memtailor
Version:        1.0
Release:        11.%{gitdate}.git%{shorttag}%{?dist}
Summary:        C++ library of special-purpose memory allocators

License:        BSD
URL:            https://github.com/%{user}/%{name}
Source0:        https://github.com/%{user}/%{name}/tarball/%{gittag}/%{user}-%{name}-%{shorttag}.tar.gz

# Upstream wants to download gtest and compile it in; we don't
Patch0:         %{name}-gtest.patch

BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libtool

%description
Memtailor is a C++ library of special purpose memory allocators.  It
currently offers an arena allocator and a memory pool.

The main motivation to use a memtailor allocator is better and more
predictable performance than you get with new/delete.  Sometimes a
memtailor allocator can also be more convenient due to the ability to
free many allocations at one time.

The Memtailor memory pool is useful if you need to do many allocations
of a fixed size.  For example a memory pool is well suited to allocate
the nodes in a linked list.

You can think of the Memtailor arena allocator as being similar to stack
allocation.  Both kinds of allocation are very fast and require you to
allocate/deallocate memory in last-in-first-out order.  Arena allocation
has the further benefits that it stays within the C++ standard, it will
not cause a stack overflow, you can have multiple arena allocators at
the same time and allocation is not tied to a function invocation.

%package devel
Summary:        Development files for memtailor
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for developing applications that use memtailor.

%prep
%setup -q -n %{user}-%{name}-%{shorttag}
%patch0

# Every file is marked executable; only a few need to be.
find . -type f -perm /0111 | xargs chmod a-x
chmod a+x autogen.sh fixspace replace

# Upstream doesn't generate the configure script
autoreconf -fi

%build
export GTEST_PATH=%{_prefix}
export GTEST_VERSION=$(gtest-config --version)
%configure --disable-static --enable-shared --with-gtest=yes

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

make %{?_smp_mflags}

%install
%make_install

# We don't want the libtool archive
rm -f %{buildroot}%{_libdir}/lib%{name}.la

%ldconfig_scriptlets

%check
export LD_LIBRARY_PATH=$PWD/.libs
make check

%files
%doc README.md
%license license.txt
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4.20160311.gite85453b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr  4 2016 Jerry James <loganjerry@gmail.com> - 1.0-3.20160311.gite85453b
- Update to latest upstream snapshot

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2.20140924.git7b48b98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jerry James <loganjerry@gmail.com> - 1.0-1.20140924.git7b48b98
- Change to Macaulay2 repo
- Revert Macaulay2 patch to disable libtool (memtailor-libtool.patch)
- Use a patch instead of sed for gtest manipulations (memtailor-gtest.patch)

* Fri Sep  4 2015 Jerry James <loganjerry@gmail.com> - 0-1.20130809.git722a30c
- Initial RPM
