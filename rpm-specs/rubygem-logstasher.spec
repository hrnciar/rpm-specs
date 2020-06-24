%global gem_name logstasher

# disable tests:
# * tests require rails < 5 (no F25+)
# * tests require rspec >= 3 (no EPEL 7)
%global with_tests 0

# use logstasher without rails (activesupport always required):
# * rails < 5 required (no F25+)
# * activerecord required (no EPEL 7)
%if 0%{?fedora} && 0%{?fedora} >= 25 || 0%{?rhel}
%global with_rails 0
%endif

Name:           rubygem-%{gem_name}
Version:        1.3.0
Release:        4%{?dist}
Summary:        Awesome rails logs

License:        MIT
URL:            https://github.com/shadabahmed/logstasher
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/shadabahmed/logstasher.git && cd logstasher
# git checkout v1.3.0
# tar -czf rubygem-logstasher-1.3.0-repo.tgz sample_logstash_configurations/ spec/ LICENSE README.md
Source1: %{name}-%{version}-repo.tgz
# bundler killer patch
# (not intended for upstream)
Patch0:         logstasher-tests-unbundle.diff

BuildArch:      noarch
BuildRequires:  rubygems-devel
%if 0%{?with_tests}
BuildRequires:  rubygem(activerecord) >= 4.0
BuildRequires:  rubygem(logstash-event) => 1.2
BuildRequires:  rubygem(rails) >= 4.0
BuildRequires:  rubygem(redis)
BuildRequires:  rubygem(request_store)
BuildRequires:  rubygem(rspec) >= 3
%endif
%if 0%{?with_rails}
# missing runtime dependency
Requires:       rubygem(actionview) >= 3.0
%endif
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(activesupport) => 4.0
%if 0%{?with_rails}
Requires:       rubygem(activerecord) => 4.0
%endif
Requires:       rubygem(logstash-event) => 1.2.0
Requires:       rubygem(logstash-event) < 1.3
# dependency of activesupport
Requires:       rubygem(minitest5)
Requires:       rubygem(request_store)
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
Logstasher gem generates logstash compatible logs in JSON format. It can also
easily log events from Rails.
%if ! 0%{?with_rails}
Logstasher is not compatible with the current version of Rails, but it is
possible to use logstasher in non-rails applications.
%endif

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}
tar xzf %{SOURCE1}
%patch0 -p1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%if ! 0%{?with_rails}
sed -e '/add_dependency.*\(rails\|activerecord\)/d' -i %{gem_name}.gemspec
%endif


%build
gem build %{gem_name}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

cp -a sample_logstash_configurations/ LICENSE README.md \
        %{buildroot}%{gem_instdir}/


%check
%if 0%{?with_tests}
cp -pr spec/ ./%{gem_instdir}
pushd .%{gem_instdir}
rspec -Ilib -Ispec spec
popd
rm -rf spec/
%endif


%files
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}/
%{gem_instdir}/sample_logstash_configurations/


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 František Dvořák <valtri@civ.zcu.cz> - 1.3.0-1
- Update to 1.3.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 07 2017 František Dvořák <valtri@civ.zcu.cz> - 1.2.1-1
- Update to 1.2.1 (#1309669)
- Removed compatibility macros for older Fedora
- Rail-less version, tests disabled

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 08 2015 František Dvořák <valtri@civ.zcu.cz> - 0.8.6-1
- Update to 0.8.6

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 František Dvořák <valtri@civ.zcu.cz> - 0.6.5-1
- Update to 0.6.5
- Patches for tests addressed by upstream

* Fri Jan 09 2015 František Dvořák <valtri@civ.zcu.cz> - 0.6.2-1
- Update to 0.6.2
- Enable tests for Rawhide (Fedora >= 22)
- Use %%license macro
- Don't package the tests

* Tue Sep 16 2014 František Dvořák <valtri@civ.zcu.cz> - 0.6.1-1
- Update to 0.6.1

* Wed Sep 10 2014 František Dvořák <valtri@civ.zcu.cz> - 0.6.0-2
- Explicit runtime dependency on activesupport

* Thu Aug 28 2014 František Dvořák <valtri@civ.zcu.cz> - 0.6.0-1
- Initial package
