%{?nodejs_default_filter}
%{?nodejs_find_provides_and_requires}

Name:       nodejs-rhea
Version:    1.0.24
Release:    1%{?dist}
Summary:    A reactive messaging library based on the AMQP protocol
License:    ASL 2.0
URL:        https://github.com/grs/rhea
Source0:    rhea-%{version}.tar.gz

BuildArch:  noarch
%if 0%{?fedora}
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging
BuildRequires:  nodejs-debug
Requires:       nodejs-debug


%description
A reactive library for the AMQP protocol.


%prep
%setup -q -n rhea-%{version}


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/rhea
cp -a lib  package.json dist .eslintrc %{buildroot}%{nodejs_sitelib}/rhea
%nodejs_symlink_deps


%check 
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
rm -fr test

%files
%license LICENSE
%doc README.md examples
%{nodejs_sitelib}/rhea


%changelog
* Thu Sep 24 2020 Irina Boverman <iboverma@redhat.com> - 1.0.24-1
- Rebased to 1.0.24

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Irina Boverman <iboverma@redhat.com> - 1.0.21-1
- Rebased to 1.0.21

* Mon Mar  2 2020 Irina Boverman <iboverma@redhat.com> - 1.0.19-1
- Rebased to 1.0.19

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  2 2019 Irina Boverman <iboverma@redhat.com> - 1.0.10-1
- Rebased to 1.0.10

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Irina Boverman <iboverma@redhat.com> - 1.0.7-1
- Rebased to 1.0.7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Irina Boverman <iboverma@redhat.com> - 0.3.9-1
- Rebased to 0.3.9

* Mon Jan  7 2019 Irina Boverman <iboverma@redhat.com> - 0.3.8-1
- Rebased to 0.3.8

* Fri Jan  4 2019 Irina Boverman <iboverma@redhat.com> - 0.3.6-1
- Rebased to 0.3.6

* Tue Jul 24 2018 Irina Boverman <iboverma@redhat.com> - 0.2.17-1
- Rebased to 0.2.17

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Irina Boverman <iboverma@redhat.com> - 0.2.15-1
- Rebased to 0.2.15

* Tue Mar 13 2018 Irina Boverman <iboverma@redhat.com> - 0.2.10-1
- Rebased to 0.2.10

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Irina Boverman <iboverma@redhat.com> - 0.2.9-1
- Rebased to 0.2.9

* Wed Nov 15 2017 Irina Boverman <iboverma@redhat.com> - 0.2.6-1
- Rebased to 0.2.6

* Fri Sep 15 2017 Irina Boverman <iboverma@redhat.com> - 0.2.4-1
- Rebased to 0.2.4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Irina Boverman <iboverma@redhat.com> - 0.2.0-1
- Rebased to 0.2.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug  1 2016 Irina Boverman <iboverma@redhat.com> - 0.1.7-1
- Rebased to 0.1.7

* Mon Jun 13 2016 Irina Boverman <iboverma@redhat.com> - 0.1.6-1
- Rebased to 0.1.6

* Tue Jun  7 2016 Irina Boverman <iboverma@redhat.com> - 0.1.5-1
- Rebased to 0.1.5

* Wed Jun  1 2016 Irina Boverman <iboverma@redhat.com> - 0.1.3-1
- Rebased to 0.1.3

* Tue May 31 2016 Irina Boverman <iboverma@redhat.com> - 0.1.2-1
- Initial package
