Name:           clinfo
Summary:        Enumerate OpenCL platforms and devices
Version:        2.2.18.04.06
Release:        4%{?dist}

License:        CC0
URL:            https://github.com/Oblomov/clinfo
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ocl-icd-devel

%description
A simple OpenCL application that enumerates all possible platform and
device properties. Inspired by AMD's program of the same name, it is
coded in pure C99 and it tries to output all possible information,
including that provided by platform-specific extensions, and not to
crash on platform-unsupported properties (e.g. 1.2 properties on 1.1
platforms).

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man1/%{name}.1

%files
%license LICENSE legalcode.txt
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.18.04.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.18.04.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.18.04.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.18.04.06-1
- Update to 2.2.18.04.06

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.17.10.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.17.10.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.17.10.25-1
- Update to 2.2.17.10.25

* Wed Aug 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.17.08.25-1
- Update to 2.2.17.08.25

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.17.06.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.17.06.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.17.06.14-1
- Update to 2.2.17.06.14

* Sat Feb 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.17.02.09-1
- Update to 2.1.17.02.09

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16.01.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.1.16.01.12-2
- Rebuild for OpenCL 2.1
- Cleanups and fixes in spec

* Sun Feb 07 2016 Fabian Deutsch <fabiand@fedoraproject.org> - 2.1.16.01.12-1.0.git20160207.f951686
- Update to the latest upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.8.git20150215.94fdb47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.7.git20150215.94fdb47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 15 2015 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1.0-0.6.git20150215.94fdb47
- Update to the latest upstream

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.5.git20140422.7050765
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.4.git20140422.7050765
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-0.3.git20140422.7050765
- Fix two bugs related to platforms without devices

* Tue Oct 01 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-0.2.git20131001.7f44937
- Remove unused ldconfig and opencl-filesystem

* Tue Oct 01 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-0.1.git20131001.7f44937
- Initial package
