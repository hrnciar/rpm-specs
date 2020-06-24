%global gem_name rack-protection

%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 2.0.8.1
Release: 1%{?dist}
Summary: Ruby gem that protects against typical web attacks
License: MIT
URL: http://sinatrarb.com/protection/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/sinatra/sinatra.git && cd sinatra/rack-protection
# git archive -v -o rack-protection-2.0.8.1-spec.tar.gz v2.0.8.1 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
# Fix test failure due to Rack 2.2.2 incompatibility.
# https://github.com/sinatra/sinatra/pull/1605
Patch0: rubygem-rack-protection-2.0.8.1-Fix-failing-tests.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{without bootstrap}
BuildRequires: rubygem(rack)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rack-test)
%endif
BuildArch: noarch

%description
Protect against typical web attacks, works with all Rack apps, including
Rails.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

pushd %{_builddir}
%patch0 -p2
popd

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



%if %{without bootstrap}
%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec

rspec -r 'spec_helper' spec
popd
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/License
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/rack-protection.gemspec

%changelog
* Tue Apr 28 2020 Vít Ondruch <vondruch@redhat.com> - 2.0.8.1-1
- Update to rack-protection 2.0.8.1.
  Resolves: rhbz#1744277
  Resolves: rhbz#1800024

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Jun Aruga <jaruga@redhat.com> - 2.0.3-1
- Update to rack-protection 2.0.3.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Jun Aruga <jaruga@redhat.com> - 2.0.0-1
- Update to rack-protection 2.0.0.

* Tue Feb 07 2017 Jun Aruga <jaruga@redhat.com> - 1.5.3-4
- Fix for RSpec 3 compatibility.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 23 2015 Vít Ondruch <vondruch@redhat.com> - 1.5.3-1
- Update to rack-protection 1.5.3.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Michal Fojtik <mfojtik@redhat.com> - 1.5.0-1
- Release 1.5.0

* Tue Mar 05 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.2-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Fri Feb 22 2013 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-2
- Fixed rspec dependency

* Thu Feb 21 2013 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-1
- Release 1.3.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-4
- Set %%bootstrap to 0 to allow tests.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-3
- Rebuilt for Ruby 1.9.3.
- Introduced bootstrap to deal with dependency loop.

* Tue Jan 03 2012 Michal Fojtik <mfojtik@redhat.com> - 1.2.0-2
- Fixed BR
- Marked documentation file with doc tag
- Changed the way how to run rspec tests

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.2.0-1
- Initial import
