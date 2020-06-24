%global gem_name yard

Name: rubygem-%{gem_name}
Version: 0.9.24
Release: 1%{?dist}
Summary: Documentation tool for consistent and usable documentation in Ruby
License: MIT and (BSD or Ruby)
URL: http://yardoc.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# The 'irb/notifier' might be required for parsing of some old Ruby code.
# https://github.com/lsegal/yard/blob/v0.9.24/lib/yard/parser/ruby/legacy/irb/slex.rb#L13
Recommends: rubygem(irb)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(RedCloth)
BuildRequires: rubygem(asciidoctor)
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(redcarpet)
BuildRequires: rubygem(rack)
BuildArch: noarch

%description
YARD is a documentation generation tool for the Ruby programming language.
It enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

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


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

# Some files in 0.9.24 release has still executable bit set :/
# https://github.com/lsegal/yard/issues/1147
find %{buildroot}%{gem_instdir} -type f | xargs chmod a-x

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}

# There are quite some test mocking File functionality which makes running the
# test suite without Bundler hard. Since the test suite includes Bundler test
# cases, just remove the unnecessary dependencies and run the test suite via
# Bundler.
sed -r -i "/(coveralls|gettext|samus|simplecov)/ s/^/#/" Gemfile

rspec spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/yard
%{_bindir}/yardoc
%{_bindir}/yri
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LEGAL
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/po
%{gem_instdir}/templates
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Dockerfile.samus
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/benchmarks
%doc %{gem_instdir}/docs
%{gem_instdir}/samus.json
%{gem_instdir}/spec
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Tue Feb 04 2020 Vít Ondruch <vondruch@redhat.com> - 0.9.24-1
- Update to YARD 0.9.24.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Vít Ondruch <vondruch@redhat.com> - 0.9.12-3
- Fix FTBFS due to failing test suite (rhbz#1556422).

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 01 2017 Vít Ondruch <vondruch@redhat.com> - 0.9.12-1
- Update to YARD 0.9.12.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Vít Ondruch <vondruch@redhat.com> - 0.9.8-1
- Update to YARD 0.9.8.

* Wed May 25 2016 Jun Aruga <jaruga@redhat.com> - 0.8.7.6-3
- Fix test suite for Ruby 2.3 compatibility. (rhbz#1308100)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 08 2015 Vít Ondruch <vondruch@redhat.com> - 0.8.7.6-1
- Update to YARD 0.8.7.6.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 03 2014 Vít Ondruch <vondruch@redhat.com> - 0.8.7.4-1
- Update to yard 0.8.7.4.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Vít Ondruch <vondruch@redhat.com> - 0.8.7-1
- Update to yard 0.8.7.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Vít Ondruch <vondruch@redhat.com> - 0.8.5.2-1
- Update to yard 0.8.5.2.

* Fri Mar 15 2013 Vít Ondruch <vondruch@redhat.com> - 0.8.2.1-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Vít Ondruch <vondruch@redhat.com> - 0.8.2.1-1
- Update to yard 0.8.2.1.

* Thu May 03 2012 Vít Ondruch <vondruch@redhat.com> - 0.8.1-1
- Update to yard 0.8.1.

* Wed Jan 25 2012 Vít Ondruch <vondruch@redhat.com> - 0.7.4-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Vít Ondruch <vondruch@redhat.com> - 0.7.4-1
- Updated to yard 0.7.4.

* Mon Jul 25 2011 Mo Morsi <mmorsi@redhat.com> - 0.7.2-1
- update to latest upstream release
- fixes to conform to fedora guidelines

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 22 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.5.3-3
- fixed dependencies/package issues according to guidelines

* Mon Feb 08 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.5.3-2
- cleaned up macros, other package guideline compliance fixes
- corrected license, added MIT
- include all files and docs, added check/test section

* Mon Feb 08 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.5.3-1
- Initial package

