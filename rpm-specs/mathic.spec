%global gitdate         20181123
%global gittag          e13b94422e3bd250523e88232138edd124793ec2
%global shorttag        %(c=%{gittag}; echo ${c:0:7})
%global user            Macaulay2

Name:           mathic
Version:        1.0
Release:        14.%{gitdate}.git%{shorttag}%{?dist}
Summary:        Data structures for Groebner basis computations

License:        LGPLv2+
URL:            https://github.com/%{user}/%{name}
Source0:        https://github.com/%{user}/%{name}/tarball/%{gittag}/%{user}-%{name}-%{shorttag}.tar.gz

# Upstream wants to download gtest and compile it in; we don't
Patch0:         %{name}-gtest.patch

BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libtool
BuildRequires:  memtailor-devel

%description
Mathic is a C++ library of fast data structures designed for use in
Groebner basis computation.  This includes data structures for ordering
S-pairs, performing divisor queries and ordering polynomial terms during
polynomial reduction.

With Mathic you get to use highly optimized code with little effort so
that you can focus more of your time on whatever part of your Groebner
basis implementation that you are interested in.  The data structures
use templates to allow you to use them with whatever representation of
monomials/terms and coefficients that your code uses.  In fact the only
places where Mathic defines its own monomials/terms is in the test code
and example code.  Currently only dense representations of
terms/monomials are suitable since Mathic will frequently ask "what is
the exponent of variable number x in this term/monomial?".

%package devel
Summary:        Development files for mathic
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       memtailor-devel%{?_isa}

%description devel
Files for developing applications that use mathic.

%package tools
Summary:        Mathic-based tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
Mathic-based tools.  Currently this contains:
- divsim: divisor query simulation
- pqsim: priority queue simulation

%prep
%setup -q -n %{user}-%{name}-%{shorttag}
%patch0

# Nearly every file is marked executable; only a few need to be.
find . -type f -perm /0111 | xargs chmod a-x
chmod a+x autogen.sh fixspace replace

# Update the C++ standard slightly
sed -i 's/-std=gnu++0x/-std=gnu++11/' Makefile.am

# Upstream doesn't generate the configure script
autoreconf -fi

%build
export GTEST_PATH=%{_prefix}
export GTEST_VERSION=$(gtest-config --version)
%configure --disable-static --enable-shared --with-gtest=yes GTEST_LIBS=-lgtest

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

make %{?_smp_mflags}
make %{?_smp_mflags} divsim pqsim

%install
%make_install

# We don't want the libtool archive
rm -f %{buildroot}%{_libdir}/lib%{name}.la

# Install the tools
mkdir -p %{buildroot}%{_bindir}
cp -p divsim pqsim %{buildroot}%{_bindir}

%check
export LD_LIBRARY_PATH=$PWD/.libs
make check

%files
%doc README.md
%license lgpl-2.1.txt
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/divsim
%{_bindir}/pqsim

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14.20181123.gite13b944
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13.20181123.gite13b944
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12.20181123.gite13b944
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Jerry James <loganjerry@gmail.com> - 1.0-11.20181123.gite13b944
- Update to latest upstream snapshot
- Add -tools subpackage for the new divsim and pqsim binaries

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10.20170606.git2f4a411
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9.20170606.git2f4a411
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Jerry James <loganjerry@gmail.com> - 1.0-8.20170606.git2f4a411
- Update to latest upstream snapshot

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7.20160320.git558fff0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6.20160320.git558fff0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5.20160320.git558fff0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr  4 2016 Jerry James <loganjerry@gmail.com> - 1.0-4.20160320.git558fff0
- Update to latest upstream snapshot

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3.20150603.git18ff8ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jerry James <loganjerry@gmail.com> - 1.0-2.20150603.git18ff8ac
- Change to Macaulay2 repo
- Revert Macaulay2 patch to disable libtool (mathic-libtool.patch)
- Use a patch instead of sed for gtest manipulations (mathic-gtest.patch)

* Fri Nov 27 2015 Jerry James <loganjerry@gmail.com> - 1.0-1.20130827.git66b5d74
- Initial RPM
