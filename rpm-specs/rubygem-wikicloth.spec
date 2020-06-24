%global gem_name wikicloth

Name: rubygem-%{gem_name}
Version: 0.8.0
Release: 13%{?dist}
Summary: Mediawiki parser
License: MIT
URL: https://github.com/nricciar/wikicloth
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Minitest 5 support
# https://github.com/nricciar/wikicloth/pull/69
Patch0: rubygem-wikicloth-0.8.0-minitest.patch
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(builder)
Requires: rubygem(expression_parser)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(expression_parser)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
An implementation of the mediawiki markup in Ruby.


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

# Minitest 5 support
# https://github.com/nricciar/wikicloth/pull/69
%patch0 -p1

# Remove developer-only files.
for f in .gitignore .travis.yml Gemfile Rakefile run_tests.rb tasks/wikicloth_tasks.rake; do
  rm $f
  sed -i "s|\"$f\".freeze,||g" %{gem_name}.gemspec
done

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%gem_install

# Remove unnecessary gemspec
rm .%{gem_instdir}/%{gem_name}.gemspec

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
  ruby -Ilib test/*_test.rb
popd


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README
%doc %{gem_instdir}/README.textile
%doc %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{gem_instdir}/init.rb
%{gem_instdir}/lang

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/test
%{gem_instdir}/examples
%{gem_instdir}/sample_documents

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Karsten Hopp <karsten@redhat.com> - 0.8.0-8
- fix sed script in spec file

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 10 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.8.0-3
- Patch for Minitest 5 (RHBZ #1107264)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 06 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.8.0-1
- Initial package
