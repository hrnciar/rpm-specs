%global gem_name childprocess

Name: rubygem-%{gem_name}
Version: 1.0.1
Release: 6%{?dist}
Summary: A gem for controlling external programs running in the background
License: MIT
URL: http://github.com/enkessler/childprocess
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix Ruby 2.6 compatibility.
# https://github.com/enkessler/childprocess/pull/149
Patch0: rubygem-childprocess-1.0.1-Rewrite-unix-fork-reopen-to-be-compatible-with-ruby-2.6.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(ffi)
BuildRequires: rubygem(rspec) >= 3
BuildArch: noarch
# posix_spaw is not implemented everywhere, use just Intel for build.
ExclusiveArch: %{ix86} x86_64 noarch

%description
This gem aims at being a simple and reliable solution for controlling external
programs running in the background on any Ruby / OS combination.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%patch0 -p1

# Disable windows specific installation of FFI gem.
sed -i "/extensions/ s/^/#/" ../%{gem_name}-%{version}.gemspec
%gemspec_remove_dep -g rake '< 13.0'
%gemspec_remove_file "ext/mkrf_conf.rb"

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

%check
pushd .%{gem_instdir}
# We don't care about code coverage.
sed -i '/[cC]overalls/ s/^/#/' spec/spec_helper.rb

# Disable validity of .gemspec check, since it requires Git and it is not super
# important.
sed -i "/gemspec.validate/ s/^/#/" spec/childprocess_spec.rb

# We need Unicode support to pass "ChildProcess allows unicode characters
# in the environment" test case.
LC_ALL=C.UTF-8 RUBYOPT=-Ilib rspec spec

# Test also posix_spawn, which requires FFI.
CHILDPROCESS_POSIX_SPAWN=true LC_ALL=C.UTF-8 RUBYOPT=-Ilib rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_cache}
%{gem_spec}


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/appveyor.yml
%{gem_instdir}/childprocess.gemspec
%{gem_instdir}/spec

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Vít Ondruch <vondruch@redhat.com> - 1.0.1-3
- Remove unnecessary Rake dependency.

* Fri Jun 07 2019 Vít Ondruch <vondruch@redhat.com> - 1.0.1-2
- posix_spaw is not implemented everywhere, use just Intel for build.

* Wed Jun 05 2019 Vít Ondruch <vondruch@redhat.com> - 1.0.1-1
- Update to childprocess 1.0.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  2 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.9-1
- 0.5.9

* Tue Mar 01 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 0.5.3-5
- BR: rubygem-rspec2 (#1308012)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 06 2015 Josef Stribny <jstribny@redhat.com> - 0.5.3-3
- Fix FTBFS: Run tests with RSpec2 bin

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 28 2014 Josef Stribny <jstribny@redhat.com> - 0.5.3-1
- Update childprocess to version 0.5.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 23 2013 Mo Morsi <mmorsi@redhat.com> - 0.3.9-1
- Update to childprocess 0.3.9

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Vít Ondruch <vondruch@redhat.com> - 0.3.6-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Mo Morsi <mmorsi@redhat.com> - 0.3.6-1
- Update to childprocess 0.3.6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 0.2.0-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 03 2011 Chris Lalancette <clalance@redhat.com> - 0.2.0-1
- Initial package
