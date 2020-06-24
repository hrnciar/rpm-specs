# Generated from elasticsearch-1.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name elasticsearch

Name: rubygem-%{gem_name}
Version: 5.0.4
Release: 6%{?dist}
Summary: Ruby integrations for Elasticsearch
License: ASL 2.0
URL: http://github.com/elasticsearch/elasticsearch-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
Requires: rubygem(elasticsearch-api) = %{version}
Requires: rubygem(elasticsearch-transport) = %{version}
# the following BuildRequires are development dependencies
# BuildRequires: rubygem(elasticsearch-extensions)
# BuildRequires: rubygem(ansi)
# BuildRequires: rubygem(shoulda-context)
# BuildRequires: rubygem(mocha)
# BuildRequires: rubygem(turn)
# BuildRequires: rubygem(yard)
# BuildRequires: rubygem(pry)
# BuildRequires: rubygem(ci_reporter) >= 1.9
# BuildRequires: rubygem(ci_reporter) < 2
# BuildRequires: rubygem(minitest) >= 4.0
# BuildRequires: rubygem(minitest) < 5
# BuildRequires: rubygem(ruby-prof)
# BuildRequires: rubygem(require-prof)
# BuildRequires: rubygem(simplecov)
# BuildRequires: rubygem(simplecov-rcov)
# BuildRequires: rubygem(cane)
# BuildRequires: rubygem(test-unit) >= 2
# BuildRequires: rubygem(test-unit) < 3
BuildArch: noarch

%if 0%{?rhel} >= 7
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
Ruby integrations for Elasticsearch (client, API, etc.).


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%license %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/elasticsearch.gemspec
%{gem_instdir}/test

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov  2 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 5.0.4-1
- Rebase on upstream 5.0.4

* Thu Jun 29 2017 Rich Megginson <rmeggins@redhat.com> - 2.0.2-1
- Bump to version 2.0.2

* Fri Sep 16 2016 Rich Megginson <rmeggins@redhat.com> - 1.0.18-1
- Bump to version 1.0.18

* Mon Mar 23 2015 Steve Traylen  <steve.traylen@cern.ch> - 1.0.8-1
- New upstream

* Thu Aug 07 2014 Steve Traylen  <steve.traylen@cern.ch> - 1.0.4-2
- Use correct time stamp for src file.

* Thu Jul 03 2014 Steve Traylen  <steve.traylen@cern.ch> - 1.0.4-1
- Initial package
