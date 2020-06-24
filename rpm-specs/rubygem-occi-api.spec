%global gem_name occi-api

# F26+: vcr >= 3.0 required
# EL7: rspec >= 3 required
%if 0%{?fedora} >= 26 || 0%{?rhel} && 0%{?rhel} <= 7
%global use_tests 0
%else
%global use_tests 1
%endif

Name:           rubygem-%{gem_name}
Version:        4.3.15
Release:        6%{?dist}
Summary:        OCCI development library providing a high-level client API

License:        ASL 2.0
URL:            https://github.com/EGI-FCTF/rOCCI-api
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch:      noarch
BuildRequires:  ruby(release) >= 1.9.3
BuildRequires:  rubygems-devel
%if 0%{?use_tests}
BuildRequires:  rubygem(httparty)
BuildRequires:  rubygem(occi-core) => 4.3.5
BuildRequires:  rubygem(occi-core) < 5
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(vcr)
BuildRequires:  rubygem(webmock) >= 1.9.3
%endif
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(release) >= 1.9.3
Requires:       ruby(rubygems)
Requires:       rubygem(occi-core) => 4.3.6
Requires:       rubygem(occi-core) < 5
Requires:       rubygem(httparty)
Requires:       rubygem(json)
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
This gem provides ready-to-use client classes to simplify the integration of
OCCI into your application.


%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
# relax dependencies (for EPEL 7)
%gemspec_remove_dep -s %{gem_name}.gemspec -g json
%gemspec_add_dep -s %{gem_name}.gemspec -g json '>= 1.7.7'


%build
gem build %{gem_name}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%check
%if 0%{?use_tests}
pushd .%{gem_instdir}
rspec -Ilib spec
popd
%endif


%files
%doc %{gem_instdir}/AUTHORS
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}/
%{gem_libdir}/
%exclude %{gem_cache}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.yardopts
%exclude %{gem_instdir}/spec/
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/%{gem_name}.gemspec
%{gem_spec}

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/examples/
%doc %{gem_instdir}/README.md


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 01 2019 František Dvořák <valtri@civ.zcu.cz> - 4.3.15-3
- Fixed FTBFS (#1606221)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 František Dvořák <valtri@civ.zcu.cz> - 4.3.15-1
- Update to 4.3.15 (#1504418)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 František Dvořák <valtri@civ.zcu.cz> - 4.3.14-1
- Update to 4.3.14 (#1481720)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 František Dvořák <valtri@civ.zcu.cz> - 4.3.13-1
- Update to 4.3.13 (#1461609)

* Tue Feb 21 2017 František Dvořák <valtri@civ.zcu.cz> - 4.3.11-2
- Relax httparty dependency

* Sun Feb 19 2017 František Dvořák <valtri@civ.zcu.cz> - 4.3.11-1
- Update to 4.3.11 (#1417327)
- Disable tests for F26+ (#1424348)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 František Dvořák <valtri@civ.zcu.cz> - 4.3.7-1
- Update to 4.3.7 (#1415859)
- Relax JSON dependency

* Tue Jul 05 2016 František Dvořák <valtri@civ.zcu.cz> - 4.3.6-1
- Update to 4.3.6 (#1352505)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 František Dvořák <valtri@civ.zcu.cz> - 4.3.5-1
- Update to 4.3.5 (#1297242)

* Fri Nov 27 2015 František Dvořák <valtri@civ.zcu.cz> - 4.3.3-1
- Update to 4.3.3 (#1285911)
- Dependencies doesn't need to be relaxed now

* Wed Jun 17 2015 František Dvořák <valtri@civ.zcu.cz> - 4.3.2-1
- Update to 4.3.2 (#1232529)

* Mon Dec 01 2014 František Dvořák <valtri@civ.zcu.cz> - 4.3.1-1
- Update to 4.3.1
- The license file marked by %%license macro
- Removed tests and build files

* Sun Sep 14 2014 František Dvořák <valtri@civ.zcu.cz> - 4.2.6-1
- Initial package
