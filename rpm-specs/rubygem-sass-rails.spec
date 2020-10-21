# Generated from sass-rails-3.2.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sass-rails

Name: rubygem-%{gem_name}
Version: 5.0.7
Release: 7%{?dist}
Summary: Sass adapter for the Rails asset pipeline
License: MIT
URL: https://github.com/rails/sass-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/sass-rails.git && cd sass-rails
# git checkout v5.0.7 && tar czvf sass-rails-5.0.7-tests.tgz ./test
Source1: sass-rails-%{version}-tests.tgz
# Fix the test suite compatibility with Rails 5.2.
# https://github.com/rails/sass-rails/pull/421
Patch0: rubygem-sass-rails-5.0.7-Rails-5-2-compatibility.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(rails)
BuildRequires: rubygem(sass)
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(tilt)
BuildArch: noarch

%description
Sass adapter for the Rails asset pipeline.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

pushd %{_builddir}
%patch0 -p1
popd

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test test

# Copy in .gemspec and use the sass-rails sources
cp %{buildroot}%{gem_spec} sass-rails.gemspec
echo 'gem "sass-rails", :path => "."' >> Gemfile

# Disable Ruby 2.7 warnings to make the test suite pass (e.g.
# SassRailsTest#test_sass_allows_compressor_override_in_test_mode). Please
# revisit with newer Rails as things should get better.
export RUBYOPT='-W:no-deprecated'

ruby -I.:test -e 'Dir.glob "test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Mon Aug 03 2020 Vít Ondruch <vondruch@redhat.com> - 5.0.7-7
- Disable Ruby 2.7 warnings to make the test suite pass.
  Resolves: rhbz#1863733

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Vít Ondruch <vondruch@redhat.com> - 5.0.7-1
- Update to sass-rails 5.0.7.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Vít Ondruch <vondruch@redhat.com> - 5.0.6-3
- Fix the test suite compativility with Rails 5.1.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 02 2016 Vít Ondruch <vondruch@redhat.com> - 5.0.6-1
- Update to sass-rails 5.0.6.

* Wed Jul 20 2016 Vít Ondruch <vondruch@redhat.com> - 5.0.5-1
- Update to sass-rails 5.0.5.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 16 2015 Vít Ondruch <vondruch@redhat.com> - 5.0.4-1
- Update to sass-rails 5.0.4.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Vít Ondruch <vondruch@redhat.com> - 5.0.3-1
- Update to sass-rails 5.0.3.

* Mon Feb 16 2015 Josef Stribny <jstribny@redhat.com> - 5.0.1-1
- Update to 5.0.1

* Tue Jul 01 2014 Vít Ondruch <vondruch@redhat.com> - 4.0.3-1
- Update to sass-rails 4.0.3.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Josef Stribny <jstribny@redhat.com> - 4.0.0-1
- Update to sass-rails 4.0.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.6-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to sass-rails 3.2.6.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.5-1
- Initial package
