%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
Name:		proxyfuzz	
Version:	20190404
Release:	16%{?dist}
Summary:	Man-in-the-middle non-deterministic network fuzzer

License:	GPLv3+
URL:		https://github.com/SECFORCE
Source0:	proxyfuzz.py
Source1:	README-Fedora

BuildArch:	noarch
Requires:	python3-twisted
BuildRequires:	python3-devel
%if 0%{?with_python3}
BuildRequires:	python3-devel
%endif # if with_python3

#Patch0:		make-executable.patch

%description
ProxyFuzz is a man-in-the-middle non-deterministic network fuzzier written in
Python. ProxyFuzz randomly changes (fuzzes) contents on the network traffic.
It supports TCP and UDP protocols and can also be configured to fuzz only one
side of the communication. ProxyFuzz is protocol agnostic so it can randomly
fuzz any network communication.

%prep
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .
#%patch0 -p1 -b .make-executable

%build

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -p -d ${RPM_BUILD_ROOT}/%{_sbindir}
install -m 755 -p proxyfuzz.py ${RPM_BUILD_ROOT}/%{_sbindir}/proxyfuzz



%files
%doc README-Fedora
%{_sbindir}/proxyfuzz


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190404-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20110923-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20110923-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20110923-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 20110923-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20110923-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20110923-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20110923-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110923-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110923-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110923-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110923-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110923-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 2 2012  Petr Sklenar <psklenar at, redhat.com> 20110923-1
- version changed
- released changed

* Thu Oct 13 2011 Petr Sklenar <psklenar at, redhat.com> 0.1-20110923
- version changed
- spec file improved
- README-Fedora created

* Wed Sep 7 2011 Petr Sklenar <psklenar at, redhat.com> 1-2
- make script being executable

* Wed Aug 31 2011 Petr Sklenar <psklenar at, redhat.com> 1-1
- Initial commit
