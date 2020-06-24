%global gem_name opennebula

Name:           rubygem-%{gem_name}
Version:        4.12.1
Release:        11%{?dist}
Summary:        OpenNebula Client API

License:        ASL 2.0
URL:            http://opennebula.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch:      noarch
BuildRequires:  rubygems-devel

%description
Libraries needed to talk to OpenNebula.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}

# bigdecimal is in independent package in Fedora.
%gemspec_add_dep -g bigdecimal
# xmlrpc was extracted into independent package in Ruby 2.4.
%gemspec_add_dep -g xmlrpc

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


# no testsuite
#%%check


%files
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/NOTICE
%dir %{gem_instdir}/
%{gem_libdir}/
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}/


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Vít Ondruch <vondruch@redhat.com> - 4.12.1-8
- Modernize .spec file.
- Add rubygem(bigdecimal) dependency, which is in independent package in Fedora.
- Add rubygem(xmlrpc) dependency, which was in Ruby 2.4 extracted into
  independent library.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 František Dvořák <valtri@civ.zcu.cz> - 4.12.1-1
- Update to 4.12.1 (#1209626)

* Sat Jan 24 2015 František Dvořák <valtri@civ.zcu.cz> - 4.10.2-1
- Update to 4.10.2

* Thu Nov 27 2014 František Dvořák <valtri@civ.zcu.cz> - 4.10.1-1
- Update to 4.10.1

* Tue Sep 16 2014 František Dvořák <valtri@civ.zcu.cz> - 4.8.0-1
- Initial package
