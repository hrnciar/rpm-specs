%global commit 8edab23fbc867adbada21378d65774c670c2aaf9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global checkout .20170711git%{shortcommit}

Summary:    Find peak OpenCL capacities like bandwidth & compute
Name:       clpeak
Version:    0.1
Release:    21%{?checkout}%{?dist}
License:    Public Domain
URL:        https://github.com/krrishnarraj/%{name}

Source0:    %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake >= 2.6
BuildRequires: opencl-headers
BuildRequires: ocl-icd-devel
BuildRequires: mesa-libGL-devel


%description
A tool which profiles OpenCL devices to find their peak capacities like
bandwidth & compute.

%prep
%setup -q -n %{name}-%{commit}


%build
mkdir build
cd build

%cmake ..

make %{?_smp_mflags}


%install
mkdir -p %{buildroot}/%{_bindir}/
install -pm0755 build/clpeak %{buildroot}%{_bindir}/


%files
%doc README.md LICENSE STATUS
%{_bindir}/clpeak


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-20.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-17.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15.20170711git8edab23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.1-14.20170711git8edab23
- Update to the latest upstream, fixes rhbz#1423267
- Include upstream fix for https://github.com/krrishnarraj/clpeak/issues/36

* Sat Jun 17 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.1-13.20170617git7904f26
- Update to the latest upstream, fixes rhbz#1423267

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12.20160207git1f90347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-11.20160207git1f90347
- Update to the latest upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10.20150215git9a39c0c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-9.20150215git9a39c0c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1-8.20150215git9a39c0c
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 17 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.1-7.20150215git9a39c0c
- Re-enable ARMv7 now headers issue is fixed

* Sun Feb 15 2015 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-6.20150215git9a39c0c
- Update to latest upstream

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5.20140603git97519a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4.20140603git97519a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-3.20140503git97519a8
- Async update to sync with upstream

* Fri Apr 25 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-2.20140425gitc0b94f2
- Improve installation
- Drop gcc-c++ BR

* Fri Apr 25 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-1.20140425gitc0b94f2
- Initial package
