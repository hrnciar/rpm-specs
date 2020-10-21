%global commit 45454b8de4ff8f860f6f78438107133e510336ed
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		puppetlabs-stdlib
Version:	4.25.1
Release:	6%{?dist}
Summary:	Puppet Labs Standard Library
License:	ASL 2.0
URL:		https://github.com/puppetlabs/puppetlabs-stdlib
Source0:	https://github.com/puppetlabs/puppetlabs-stdlib/archive/%{commit}/puppetlabs-stdlib-%{shortcommit}.tar.gz
BuildArch:	noarch
Requires:	puppet >= 2.7.0

%description
Puppet Labs Standard Library module.

%prep
%setup -qn %{name}-%{commit}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/puppet/modules/stdlib
cp -rp lib/ %{buildroot}/%{_datadir}/puppet/modules/stdlib/lib
cp -rp spec/ %{buildroot}/%{_datadir}/puppet/modules/stdlib/spec
cp -rp manifests/ %{buildroot}/%{_datadir}/puppet/modules/stdlib/manifests
cp -rp types/ %{buildroot}/%{_datadir}/puppet/modules/stdlib/types
cp -p metadata.json %{buildroot}/%{_datadir}/puppet/modules/stdlib/


%files
%doc MAINTAINERS.md CONTRIBUTING.md CHANGELOG.md README.md README_DEVELOPER.markdown
%license LICENSE
%{_datadir}/puppet/modules/stdlib

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.25.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.25.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.25.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Andrea Veri <averi@fedoraproject.org> - 4.25.1-1
- New upstream release.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-7.20150121git7a91f20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-6.20150121git7a91f20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-5.20150121git7a91f20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-4.20150121git7a91f20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-3.20150121git7a91f20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 04 2015 Andrea Veri <averi@fedoraproject.org> - 4.5.1-2.20150121git7a91f20
- Make sure metadata.json gets installed correctly for Puppet to actually
  recognize the module release version. Thanks Simon Lukasik for the patch.

* Wed Jan 21 2015 Andrea Veri <averi@fedoraproject.org> - 4.5.1-1.20150121git7a91f20
- New upstream release. (Fixes CVE-2015-1029, Red Hat's BZ #1182578)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2.20140510git08b00d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Andrea Veri <averi@fedoraproject.org> - 4.2.1-1.20140510git08b00d9
- New upstream release.

* Fri May 09 2014 Andrea Veri <averi@fedoraproject.org> - 4.2.0-1.20140509gitf3be3b6
- New upstream release.
- Drop add-missing-shebangs.patch as it was applied upstream.

* Wed May 07 2014 Andrea Veri <averi@fedoraproject.org> - 4.1.0-1.20140507gite962b95
- Initial package release.
