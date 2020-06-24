%global commit aeb8d6843cbf95149af8d66b06ca5b82aed1268f
%global shortcommit %(c=%{commit}; echo ${c:0:7})


Name:           irma_configuration
Version:        0.1
Release:        0.15.%{shortcommit}%{?dist}
Summary:        IRMA Card configuration data

License:        CC0
URL:            https://github.com/credentials/irma_configuration
Source0:        https://github.com/credentials/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:      noarch

#BuildRequires:  
#Requires:       

%description
Configuration of issuers and verifiers in the public IRMA system.

This package is used by other packages that want to verify/issue IRMA cards.


%prep
%setup -q -n %{name}-%{commit}

%build

%install
# generate_keys.sh makes no sense at all in a system-wide package
rm -f generate_keys.sh
mkdir -p %{buildroot}%{_datadir}/%{name}
# We need everything except for generate_keys.sh and README.md
cp -pr * %{buildroot}%{_datadir}/%{name}
# We only delete these ones from here because they are installed as documentation
rm -f %{buildroot}%{_datadir}/%{name}/{README.md,AUTHORS,LICENSE}

%files
%doc README.md AUTHORS LICENSE
%attr(-,root,root) %{_datadir}/%{name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.15.aeb8d68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.14.aeb8d68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.13.aeb8d68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.12.aeb8d68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1-0.11.aeb8d68
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.10.aeb8d68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.9.aeb8d68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.8.aeb8d68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.7.aeb8d68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.6.aeb8d68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 03 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.1-0.5.aeb8d68
- Fix permissions

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.4.aeb8d68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 14 2014 Patrick Uiterwijk (LOCAL) <puiterwijk@redhat.com> - 0.1-0.3.aeb8d68
- Using %%attr(0644, root, root)

* Wed Mar 12 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.1-0.2.aeb8d68
- Using shortcommit in version
- Set permissions explicitely

* Tue Mar 11 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.1-0.1.9c3105d863739a43bb13a51721bcd73a5fa75e18
- Initial Package
