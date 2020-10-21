# Generated from cucumber-wire-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-wire

%{?_with_bootstrap: %global bootstrap 1}

Name: rubygem-%{gem_name}
Version: 0.0.1
Release: 13%{?dist}
Summary: Wire protocol for Cucumber
License: MIT
URL: http://cucumber.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix compatibility with Cucumber 3.1+
# https://github.com/cucumber/cucumber-ruby-wire/pull/14
Patch0: rubygem-cucumber-wire-0.0.1-Adapt-to-the-move-of-Location-to-Cucumber-Core-Test.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if ! 0%{?bootstrap}
# Dependencies for %%check
BuildRequires: rubygem(aruba)
BuildRequires: rubygem(cucumber)
BuildRequires: rubygem(rspec)
%endif
BuildArch: noarch

%description
Wire protocol for Cucumber.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%patch0 -p1
%gemspec_add_file 'lib/cucumber/wire/step_argument.rb'

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%if ! 0%{?bootstrap}
%check
pushd .%{gem_instdir}
LANG=C.UTF-8 rspec spec

# Ensure the current version of cucumber-wire is used in place of system one,
# pulled in as a Cucumber dependency.
RUBYOPT="-I$(pwd)/lib" cucumber
popd
%endif

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/cucumber-wire.gemspec
%{gem_instdir}/features
%{gem_instdir}/spec

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 Vít Ondruch <vondruch@redhat.com> - 0.0.1-9
- Remove the test suite hack made obsolete by proper fix in rubygem-cucumber.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Vít Ondruch <vondruch@redhat.com> - 0.0.1-7
- Fix compatibility with Cucumber 3.1+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.1-3
- Fix Ruby 2.4 compatibility.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 05 2016 Vít Ondruch <vondruch@redhat.com> - 0.0.1-1
- Initial package
