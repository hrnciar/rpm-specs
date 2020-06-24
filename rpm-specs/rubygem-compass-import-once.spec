# Generated from compass-import-once-1.0.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name compass-import-once

Name: rubygem-%{gem_name}
Version: 1.0.5
Release: 13%{?dist}
Summary: Speed up your Sass compilation by making @import only import each file once
License: MIT
URL: https://github.com/chriseppstein/compass/tree/master/import-once
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# http://github.com/compass/compass/issue/1828
# backported to compass 1.0.1
Patch0: minitest5-import-once-1.0.1.patch

BuildRequires: rubygems-devel 
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(sass)
#BuildRequires: rubygem(sass-globbing) # not yet packaged
BuildRequires: rubygem(diff-lcs)
BuildArch: noarch

%description
Changes the behavior of Sass's @import directive to only import a file once.

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

%patch0 -p1

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# remove uneccessary files
pushd %{buildroot}%{gem_instdir}
rm .gitignore Gemfile* *.gemspec Rakefile
popd


# Run the test suite
%check
pushd .%{gem_instdir}
sed -i '/sass-globbing/ s/^/#/' test/test_helper.rb
mv test/fixtures/with_globbing.scss{,.disable}
ruby -Ilib:test test/import_once_test.rb
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt
%{gem_instdir}/VERSION

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/test

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 05 2015 Mo Morsi <mmorsi@redhat.com> - 1.0.5-4
- Remove sass-globbing dep to run tests
- Apply patch in prep section

* Wed Sep 17 2014 Mo Morsi <mmorsi@redhat.com> - 1.0.5-3
- Run tests

* Thu Aug 28 2014 Mo Morsi <mmorsi@redhat.com> - 1.0.5-2
- Remove uneeded Requires
- Add VERSION to main package

* Thu Aug 21 2014 Mo Morsi <mmorsi@redhat.com> - 1.0.5-1
- Initial package
