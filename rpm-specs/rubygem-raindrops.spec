%global gem_name raindrops


Summary: Real-time stats for preforking Rack servers
Name: rubygem-%{gem_name}
Version: 0.13.0
Release: 18%{?dist}
License: LGPLv2 or LGPLv3
URL: http://raindrops.bogomips.org/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Ruby 2.3 compatibility workaround.
# https://bugs.ruby-lang.org/issues/12034
Patch0: rubygem-raindrops-0.15.0-linux-workaround-Ruby-2.3-change.patch
BuildRequires: ruby(release)
BuildRequires: gcc
BuildRequires: ruby-irb
BuildRequires: rubygems-devel
#BuildRequires: rubygem(unicorn) will be included after bootstrapping unicorn
BuildRequires: rubygem(rack)
BuildRequires: rubygem(minitest)
BuildRequires: ruby-devel
ExcludeArch:   ppc ppc64

%description
Raindrops is a real-time stats toolkit to show statistics for Rack HTTP
servers.  It is designed for preforking servers such as Rainbows! and
Unicorn, but should support any Rack HTTP server under Ruby 1.9, 1.8 and
Rubinius on platforms supporting POSIX shared memory.  It may also be
used as a generic scoreboard for sharing atomic counters across multiple
processes.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for %{name}


%prep

%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p1
popd

# Adjusting minor permissions
chmod a+r .%{gem_instdir}/ChangeLog
chmod a+r .%{gem_instdir}/NEWS
chmod a-x .%{gem_instdir}/examples/linux-listener-stats.rb

# Fixing test-suite files
sed -i '2 i\
require "rubygems"' .%{gem_instdir}/test/rack_unicorn.rb

sed -i '2 i\
require "rubygems"' .%{gem_instdir}/test/test_linux_ipv6.rb

sed -i '2 i\
require "rubygems"' .%{gem_instdir}/test/test_watcher.rb

%build

%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext
rm -f %{buildroot}%{gem_instdir}/.document
rm -f %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/.manifest
rm -f %{buildroot}%{gem_instdir}/.wrongdoc.yml
rm -f %{buildroot}%{gem_instdir}/GIT-VERSION-FILE
rm -f %{buildroot}%{gem_instdir}/GIT-VERSION-GEN
rm -f %{buildroot}%{gem_instdir}/GNUmakefile
rm -f %{buildroot}%{gem_instdir}/Rakefile
rm -f %{buildroot}%{gem_instdir}/Gemfile
rm -f %{buildroot}%{gem_instdir}/setup.rb
rm -f %{buildroot}%{gem_instdir}/pkg.mk
rm -f %{buildroot}%{gem_instdir}/raindrops.gemspec
rm -rf %{buildroot}%{gem_instdir}/.yardoc

# move header files, C extension files to the correct directory
install -d -m0755 %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/



%check
pushd .%{gem_instdir}

# Tests in troubles
rm test/test_watcher.rb
rm test/test_linux_ipv6.rb
rm test/test_middleware_unicorn_ipv6.rb
rm test/test_middleware_unicorn.rb
rm test/test_raindrops.rb
rm test/test_middleware.rb

# To run the tests using minitest 5
ruby -rminitest/autorun -rrubygems -Ilib:test:$(dirs +1)%{gem_extdir_mri} - << \EOF
  module Kernel
    alias orig_require require
    remove_method :require

    def require path
      orig_require path unless path == 'test/unit'
    end

    def assert_nothing_raised
      yield
    end
  end
  Test = Minitest
  Dir.glob "./test/test_*.rb", &method(:require)
EOF

popd

%files
%{gem_extdir_mri}
%doc %{gem_instdir}/README
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/COPYING
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec} 

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/NEWS
%doc %{gem_instdir}/LATEST
%doc %{gem_instdir}/TODO
%doc %{gem_instdir}/ChangeLog
%{gem_instdir}/examples
%{gem_instdir}/test


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.13.0-15
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.13.0-12
- F-30: rebuild against ruby26
- Add BuildRequires: gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.13.0-9
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.13.0-8
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Vít Ondruch <vondruch@redhat.com> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Mon Feb 08 2016 Vít Ondruch <vondruch@redhat.com> - 0.13.0-3
- Fix Ruby 2.3 compatibility.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 18 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.13.0-1
- 0.13.0 (ruby 2.2 support)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Josef Stribny <jstribny@redhat.com> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.10.0-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Mon Feb 04 2013 Guillermo Gómez <guillermo.gomez@gmail.com> - 0.10.0-1
- Update to last release

* Fri Feb 10 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 0.8.0-5
- Fixed spec file for Fedora Ruby 1.9 packaging guidelines

* Wed Feb 08 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 0.8.0-4
- Spec file adjusted for Fedora Ruby 1.9 packaging guidelines

* Sun Jan 22 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 0.8.0-3
- C extension moved to richt place

* Sun Jan 22 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 0.8.0-2
- License field fixed

* Sun Jan 08 2012 Guillermo Gómez <guillermo.gomez@gmail.com> - 0.8.0-1
- Initial package
