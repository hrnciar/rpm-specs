# Get post-release fixes
%global owner    freetdi
%global project  gala
%global gittag   ec2df026a2e7e83e55bf35352dc2f22a4d8b9541
%global shorttag %(cut -b -7 <<< %{gittag})
%global gitdate  20191212

Name:           %{owner}-%{project}
Version:        0
Release:        4.%{gitdate}.%{shorttag}%{?dist}
Summary:        C++ graph abstraction with low-level access

License:        GPLv3+
URL:            https://github.com/%{owner}/%{project}
Source0:        %{url}/archive/%{gittag}/%{project}-%{shorttag}.tar.gz
# Convert from the obsolete stx to tlx
# https://github.com/freetdi/gala/pull/3
Patch0:         %{name}-stx-to-tlx.patch
# Fix FTBFS on 32-bit platforms due to lack of __int128
Patch1:         %{name}-32bit.patch
# Add a missing include in graph.h
Patch2:         %{name}-graph.patch
# Implicit copy constructor with explicit assignment operator is deprecated
Patch3:         %{name}-deprecated.patch
# Remove tautological asserts
Patch4:         %{name}-always-true.patch
# Fix is_set with recent versions of boost
Patch5:         %{name}-is-set.patch

BuildArch:      noarch
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(tlx)

%description
Gala is a C++ graph implementation inspired by boost/BGL, but with low
level access.  You choose the containers and data types and get full
access -- at your own risk.

%package        devel
Summary:        C++ graph abstraction with low-level access
Provides:       %{name}-static = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       tlx-devel%{?_isa}

%description    devel
Gala is a C++ graph implementation inspired by boost/BGL, but with low
level access.  You choose the containers and data types and get full
access -- at your own risk.

%prep
%autosetup -p1 -n %{project}-%{gittag}

# Preserve timestamps
sed -i 's/INSTALL = install/& -p/' Makefile

# The tests build a binary named concepts, which g++ tries to include instead of
# the C++ header named concepts when building the other tests.
mv tests/concepts.cc tests/test-concepts.cc
sed -i 's/concepts/test-concepts/' tests/Makefile

%build
# The configure script is not autotools-based.  Do NOT use %%configure!
./configure --prefix=%{_prefix}

%install
%make_install

%check
make check LOCAL_CXXFLAGS="%{optflags} -DHAVE_TLX_CONTAINER_BTREE_SET_HPP $RPM_LD_FLAGS"

%files devel
%doc README
%{_includedir}/%{project}/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20191212.ec2df02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Jerry James <loganjerry@gmail.com> - 0-3.20191212.ec2df02
- Add -graph, -deprecated, -always-true, and -is-set patches

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20191212.ec2df02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Jerry James <loganjerry@gmail.com> - 0-1.20191212.ec2df02
- Initial RPM
