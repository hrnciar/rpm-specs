Name:           libkdtree++
Version:        0.7.0
Release:        27%{?dist}
Summary:        C++ template container implementation of kd-tree sorting
URL:            http://libkdtree.alioth.debian.org/
License:        Artistic 2.0
BuildRequires:  gcc-c++
BuildRequires:  autoconf automake python3-devel swig

Source0:        http://alioth.debian.org/frs/download.php/2702/libkdtree++-0.7.0.tar.bz2

# patch to make GCC 4.7 happy (fixed in upstream git, not yet in release):
Patch0:         libkdtree++-0.7.0-pedantic.patch
# patch to make pkgconfig file (.pc) (submitted to upstream mailing list
# on 29-Sep-2012):
Patch1:         libkdtree++-0.7.0-pkgconfig.patch
# patch to build examples/test with optflags
Patch2:         libkdtree++-0.7.0-examples-optflags.patch
# patch to build with GCC 5 or later, from Debian bug 777951
Patch3:         libkdtree++-0.7.0-gcc5.patch
# patch for Python 3 compatibility, portions from Debian
Patch4:         libkdtree++-0.7.0-py3.patch

%description
%{summary}.


%package devel
Summary:        C++ template container implementation of kd-tree sorting
Provides:       libkdtree++-static = %{version}
BuildArch:      noarch

%description devel
%{summary}.


%package -n python3-libkdtree++
Provides: %{name}-python3%{?_isa} = %{version}-%{release}
Summary:        Python3 language bindings for libkdtree++

%description -n python3-libkdtree++
%{summary}.


%package examples
Summary:        Examples for libkdtree++
Requires:       libkdtree++-devel = %{version}
BuildArch:      noarch

%description examples
%{summary}.


%prep
%setup -q -n %{name}_%{version}
%patch0 -p1 -b .pkgconfig
%patch1 -p1 -b .pkgconfig
%patch2 -p1 -b .examples-optflags
%patch3 -p1 -b .gcc5
%patch4 -p1 -b .py3

# convert files from ISO-8859-1 to UTF-8 encoding
for f in README
do
  iconv -fiso88591 -tutf8 $f >$f.new
  touch -r $f $f.new
  mv $f.new $f
done


%build
autoreconf -f -i
%configure
make

cd python-bindings
make CPPFLAGS="%{optflags} -fPIC `pkg-config --cflags python3`"
cd ..

%check
cd examples
make %{?_smpflags} CPPFLAGS="%{optflags}"
./test_kdtree
./test_hayne
cd ..

cd python-bindings
python3 py-kdtree_test.py
cd ..

%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}%{python3_sitearch}
install -pm 0755 python-bindings/_kdtree.so %{buildroot}%{python3_sitearch}/
install -d %{buildroot}%{python3_sitelib}
install -pm 0644 python-bindings/kdtree.py %{buildroot}%{python3_sitelib}/

%files devel
%doc COPYING AUTHORS README NEWS TODO ChangeLog
%{_includedir}/kdtree++/
%{_datadir}/pkgconfig/*.pc

%files -n python3-libkdtree++
%doc COPYING AUTHORS README NEWS TODO ChangeLog
%{python3_sitearch}/_kdtree.so
%{python3_sitelib}/kdtree.py
%{python3_sitelib}/__pycache__/*

%files examples
%doc examples/CMakeLists.txt
%doc examples/Makefile
%doc examples/test*.cpp

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-26
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-24
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-23
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Eric Smith <brouhaha@fedoraproject.org> - 0.7.0-21
- Added Debian's patch for GCC 5 and newer.
- Add Python 3 bindings and drop Python 2 bindings

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-17
- Python 2 binary package renamed to python2-libkdtree++
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.7.0-14
- Rebuild due to bug in RPM (RHBZ #1468476)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 14 2012 Eric Smith <brouhaha@fedoraproject.org> - 0.7.0-4
- Updated based on package review.

* Sat Sep 29 2012 Eric Smith <brouhaha@fedoraproject.org> - 0.7.0-3
- Updated based on package review.

* Fri Jun 22 2012 Eric Smith <brouhaha@fedoraproject.org> - 0.7.0-2
- Updated based on package review.

* Sat Dec 03 2011 Eric Smith <brouhaha@fedoraproject.org> - 0.7.0-1
- Initial version
