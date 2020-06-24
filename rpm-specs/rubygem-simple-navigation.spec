%global gem_name simple-navigation


Summary: Ruby library for creating navigation for your Rails or Sinatra application
Name: rubygem-%{gem_name}
Version: 4.1.0
Release: 1%{?dist}
License: MIT
URL: http://github.com/codeplant/simple-navigation
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec-rails)
BuildRequires: rubygem(rails)
BuildRequires: rubygem(capybara)
BuildRequires: rubygem(memfs) => 0.4.1
# BuildRequires: rubygem(memfs) < 0.5
BuildRequires: rubygem(rspec) => 3.0
BuildRequires: rubygem(rails-deprecated_sanitizer)
BuildArch: noarch

%description
With the simple-navigation gem installed you can easily create multilevel
navigation for your Rails, Sinatra or Padrino applications. The navigation is
global in a single configuration file. It supports automatic as well as
explicit highlighting of the currently active navigation through regular
expressions.


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
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# We don't care about coverage.
sed -i '/[Cc]overalls/ s/^/#/' spec/spec_helper.rb
# Do not use bundler to require deps
sed -i '/[Bb]undler/ s/^/#/' spec/spec_helper.rb
# html-scanner was removed from rails in 4.2
# Use rails-deprecated_sanitize
sed -i '1s/^/require "rails-deprecated_sanitizer"\n/' spec/spec_helper.rb

rspec spec
popd

%files
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/gemfiles
%{gem_instdir}/generators
%{gem_libdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/spec
%{gem_instdir}/Gemfile
%{gem_instdir}/Guardfile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/*.rb
%doc %{gem_docdir}


%changelog
* Sun Jun 14 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 4.1.0-1
- Update version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 07 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 4.0.5-1
- Update version

* Tue Mar 07 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 4.0.4-1
- Update version

* Thu Jan 12 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 4.0.3-1
- Update to simple-navigation 4.0.3-1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 24 2015 Vít Ondruch <vondruch@redhat.com> - 3.14.0-1
- Update to simple-navigation 3.14.0.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Vít Ondruch <vondruch@redhat.com> - 3.10.0-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to simple-navigation 3.10.0.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Vít Ondruch <vondruch@redhat.com> - 3.5.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 19 2011 Vít Ondruch <vondruch@redhat.com> - 3.5.1-1
- Updated to simple-navigation 3.5.1.

* Fri Nov 18 2011 Vít Ondruch <vondruch@redhat.com> - 3.5.0-2
- Removed forgotten Sinatra BR.

* Fri Nov 18 2011 Vít Ondruch <vondruch@redhat.com> - 3.5.0-1
- Updated to simple-navigation 3.5.0.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Michal Fojtik <mfojtik@redhat.com> - 3.0.0-3
- Created -doc subpackage
- Fixed version dependencies
- Removed unused macros

* Sat Oct 02 2010 Michal Fojtik <mfojtik@redhat.com> - 3.0.0-2
- Added action_controller dependency

* Sat Oct 02 2010 Michal Fojtik <mfojtik@redhat.com> - 3.0.0-1
- Initial package
