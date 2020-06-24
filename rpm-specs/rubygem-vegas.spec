%global gem_name vegas

Name: rubygem-%{gem_name}
Version: 0.1.11
Release: 12%{?dist}
Summary: Create executable versions of Sinatra/Rack apps
License: MIT
URL: http://code.quirkey.com/vegas/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(bacon)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(sinatra)
BuildRequires: rubygem(thin)
BuildArch: noarch

%description
Vegas aims to solve the simple problem of creating executable versions of
Sinatra/Rack apps. It includes a class Vegas::Runner that wraps Rack/Sinatra
applications and provides a simple command line interface and launching
mechanism.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# Remove developer-only file.
rm Rakefile
sed -i -r 's|"Rakefile"(\.freeze)?,||g' %{gem_name}.gemspec

# Remove deprecated mocha statements.
# https://github.com/quirkey/vegas/pull/20
sed -i -e "s|mocha/standalone|mocha/api|" test/test_helper.rb
sed -i -e "s|mocha/object|mocha/setup|" test/test_helper.rb

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%gem_install

# Remove unnecessary gemspec
rm -rf .%{gem_instdir}/%{gem_name}.gemspec

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Skip unit test as a temporary workaround, as Mocha 1.9.0 does not work
# with Bacon until vegas will use other testing framework such as RSpec
# https://github.com/quirkey/vegas/issues/27
#
# Mocha 1.9.0 does not work with Bacon that is a project suspending
# the development. Mocha is heavily used in the test.
# https://github.com/freerange/mocha
# ruby -Ilib:test test/test_vegas_runner.rb

# Check only the requirement and the version as an alternative test.
[ "$(ruby -I lib -r vegas -e 'puts Vegas::VERSION' 2> /dev/null)" = '%{version}' ]
popd


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.rdoc
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%exclude %{gem_instdir}/test

%changelog
* Fri Feb 21 2020 Jun Aruga <jaruga@redhat.com> - 0.1.11-12
- Skip unit test as a temporary workaround, as Mocha does not work with Bacon.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 04 2018 Vít Ondruch <vondruch@redhat.com> - 0.1.11-7
- Fix FTBFS (rhbz#1556417) and small .spec file cleanup.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 06 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.1.11-1
- Initial package
