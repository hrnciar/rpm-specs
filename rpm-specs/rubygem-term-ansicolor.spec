%global gem_name term-ansicolor

Name:           rubygem-%{gem_name}
Version:        1.4.0
Release:        8%{?dist}
Summary:        Ruby library that colors strings using ANSI escape sequences
License:        GPLv2
URL:            http://flori.github.com/term-ansicolor
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 2.0
BuildRequires:  rubygem(minitest) > 5
BuildArch:      noarch

%description
This library uses ANSI escape sequences to control the attributes of terminal
output.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c  -T
%gem_install -n %{SOURCE0}


%build


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Fix permissions.
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod g-w
chmod g-w %{buildroot}%{gem_instdir}/examples/example.rb

# Remove empty hidden file.
rm %{buildroot}%{gem_libdir}/term/ansicolor/.keep


%check
pushd .%{gem_instdir}
# To run the tests using minitest 5. Upstream uses "minitest_tu_shim" for this
# purpose.
ruby -Ilib:tests -rminitest/autorun - << \EOF
  module Kernel
    alias orig_require require
    remove_method :require

    def require path
      orig_require path unless path == 'test/unit'
    end

  end

  Test = Minitest

  Dir.glob "./tests/**/*_test.rb", &method(:require)
EOF
popd

%files
%dir %{gem_instdir}
%{_bindir}/term_cdiff
%{_bindir}/term_colortab
%{_bindir}/term_decolor
%{_bindir}/term_display
%{_bindir}/term_mandel
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/COPYING
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/VERSION
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/term-ansicolor.gemspec
%{gem_instdir}/tests

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Vít Ondruch <vondruch@redhat.com> - 1.4.0-1
- Update to term-ansicolor 1.4.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 07 2014 Vít Ondruch <vondruch@redhat.com> - 1.3.0-3
- Fix FTBFS in Rawhide (rhbz#1107255).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 03 2014 Vít Ondruch <vondruch@redhat.com> - 1.3.0-1
- Update to term-ansicolor 1.3.0.

* Fri Aug 23 2013 Vít Ondruch <vondruch@redhat.com> - 1.2.2-3
- Add rubygem-tins dependency (rhbz#972544).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Vít Ondruch <vondruch@redhat.com> - 1.0.7-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.7-3
- Rebuilt for Ruby 1.9.3.
- Introduced %%check section for running tests.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 15 2011 Jan Klepek <jan.klepek at, gmail.com> - 1.0.7-1
- updated to latest version

* Sat Jul 23 2011 Jan Klepek <jan.klepek at, gmail.com> - 1.0.6-2
- removed cdiff/decolor due to conflict with colordiff package

* Sat Jul 23 2011 Jan Klepek <jan.klepek at, gmail.com> - 1.0.6-1
- New version

* Mon Mar 07 2011 Michal Fojtik <mfojtik@redhat.com> - 1.0.5-1
- Version bump

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 1.0.3-3
- Get rid of duplicate files (thanks to Mamoru Tasaka)

* Mon Jun 08 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 1.0.3-2
- Fix up documentation list
- Use gem_instdir macro where appropriate
- Do not move examples around
- Depend on ruby(abi)
- Replace defines with globals

* Fri Jun 05 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 1.0.3-1
- Package generated by gem2rpm
- Strip useless shebangs
- Move examples into documentation
- Fix up License
