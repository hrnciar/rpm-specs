Name:           ann
Version:        1.1.2
Release:        16%{?dist}
Summary:        Library for searching Approximate Nearest Neighbors

License:        LGPLv2+
URL:            http://www.cs.umd.edu/~mount/ANN
Source0:        http://www.cs.umd.edu/~mount/ANN/Files/%{version}/%{name}_%{version}.tar.gz
Patch0:         ann-make.patch
Patch1:         ann-gcc43.patch
BuildRequires:  gcc-c++


%description
ANN is a library written in the C++ programming language to support both
exact and approximate nearest neighbor searching in spaces of various
dimensions.  It was implemented by David M. Mount of the University of
Maryland, and Sunil Arya of the Hong Kong University of Science and
Technology.  ANN (pronounced like the name ``Ann'') stands for
Approximate Nearest Neighbors.  ANN is also a testbed containing
programs and procedures for generating data sets, collecting and
analyzing statistics on the performance of nearest neighbor algorithms
and data structures, and visualizing the geometric structure of these
data structures.

%package libs
Summary:        Runtime files for the ANN library

%description libs
Runtime files needed to use ANN library.

%package devel
Summary:        Development files for the ANN library
Requires:       %{name}-libs = %{version}-%{release}

%description devel
Development files needed to use ANN library.


%prep
%setup -q -n %{name}_%{version}
%patch0 -p1 -b .make
%patch1 -p1 -b .gcc43


%build
make %{?_smp_mflags} linux CFLAGS="-fPIC -DPIC $RPM_OPT_FLAGS"


%install
mkdir -p $RPM_BUILD_ROOT%{_includedir}/ANN
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -p -m 0644 include/ANN/*.h $RPM_BUILD_ROOT%{_includedir}/ANN
install -p -m 0755 lib/libANN.so.* $RPM_BUILD_ROOT%{_libdir}
install -p -m 0755 bin/ann2fig $RPM_BUILD_ROOT%{_bindir}

pushd $RPM_BUILD_ROOT%{_libdir}
ln -s libANN.so.1.0 libANN.so.1
ln -s libANN.so.1.0 libANN.so
popd

# create pkg-config file
cat << EOF > $RPM_BUILD_ROOT%{_libdir}/pkgconfig/%{name}.pc
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: %{name}
Description: Library for searching Approximate Nearest Neighbors
Version: %{version}
Requires:
Libs: -L\${libdir} -lANN
Cflags: -I\${includedir}
EOF


%files
%{_bindir}/*

%files libs
%doc Copyright.txt License.txt ReadMe.txt
%{_libdir}/*.so.*

%files devel
%doc doc/ANNmanual.pdf
%{_includedir}/ANN
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.2-6
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 18 2013 Dan Horák <dan[at]danny.cz> - 1.1.2-3
- add pkg-config file (#997212)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.1.2-1
- Upstream update.
- Rebase patches.
- Modernize spec.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-7
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 16 2008 Dan Horak <dan[at]danny.cz> - 1.1.1-2
- put general docs only into libs subpackage
- update license

* Thu Aug 14 2008 Dan Horak <dan[at]danny.cz> - 1.1.1-1
- initial Fedora package
