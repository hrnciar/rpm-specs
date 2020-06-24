# Generated from benchmark-ips-2.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name benchmark-ips

Name: rubygem-%{gem_name}
Version: 2.7.2
Release: 8%{?dist}
Summary: An iterations per second enhancement to Benchmark
License: MIT
URL: https://github.com/evanphx/benchmark-ips
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# Test dependencies
%if 0%{?rhel} == 7
BuildRequires: rubygem(minitest5)
%else
BuildRequires: rubygem(minitest)
%endif
BuildRequires: rubygem(hoe)
BuildArch: noarch
%if 0%{?rhel} == 7
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
An iterations per second enhancement to Benchmark.


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




# Run the test suite
%check
pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/README.md
%exclude %{gem_instdir}/.autotest
%exclude %{gem_instdir}/Gemfile.lock
%exclude %{gem_cache}
%{gem_instdir}/Manifest.txt
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Greg Hellings <greg.hellings@gmail.com> - 2.7.2-1
- New upstream version 2.7.2

* Thu May 12 2016 Greg Hellings <greg.hellings@gmail.com> - 2.6.1-1
- New upstream version

* Wed Mar 02 2016 Greg Hellings <greg.hellings@gmail.com> - 2.5.0-1
- Updated to upstream
- Responded to code review

* Mon Feb 08 2016 Greg Hellings <greg.hellings@gmail.com> - 2.3.0-1
- Initial package
