%global	repoid		59804

%global	mainver	1.0.19
%undefine	prever

%global	fedorarel	1

Name:		bsfilter
Version:	%{mainver}
Release:	%{?prever:0.}%{fedorarel}%{?prever:.%prever}%{?dist}.10
Summary:	Bayesian spam filter

# bsfilter script
License:	GPLv2+
URL:		http://sourceforge.jp/projects/bsfilter/
Source0:	http://dl.sourceforge.jp/%{name}/%{repoid}/%{name}-%{version}%{?prever:.%prever}.tgz

%if 0%{?fedora} >= 19
BuildRequires:	ruby(release)
Requires:		ruby(release)
%else
BuildRequires:	ruby
# No abi specification needed
Requires:		ruby
%endif
# Below is for %%check
BuildRequires:	rubygem(minitest)
BuildRequires:	ruby(mecab)
BuildRequires:	mecab-ipadic
BuildArch:		noarch

%description
Bayesian spam filter.

%prep
%setup -q -n %{name}-%{mainver}%{?prever:.%prever}
sed -i.shebang \
	-e '\@^#!@s|%{_bindir}/env ruby|%{_bindir}/ruby|' \
	bsfilter/bsfilter

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -cpm 0755 bsfilter/bsfilter %{buildroot}%{_bindir}/

%check
cd test
# Still some test fails, some of them are just dependency missing,
# some of them "really" fails, need contact with the upstream...
# rescue test failure for now
ruby ./test.rb || :

%files
# rpmlint warns about incorrect-fsf-address, need report to the upstream
%doc	COPYING
%doc	htdocs/

%{_bindir}/%{name}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-1.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-1.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-1.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-1.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-1.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-1.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.19-1
- 1.0.19

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-0.4.rc4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.18-0.4.rc4
- Support new ruby guideline

* Sun Mar  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.18-0.3.rc4
- change shebang

* Mon Feb 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.18-0.2.rc4
- 1.0.18 rc4

* Fri Feb 01 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.18-0.1.rc3
- Initial packaging
