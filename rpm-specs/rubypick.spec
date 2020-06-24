Summary: Stub to allow choosing Ruby runtime
Name: rubypick
Version: 1.1.1
Release: 12%{?dist}
License: MIT
URL: https://github.com/bkabrda/rubypick
Source0: https://github.com/bkabrda/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires: ruby(runtime_executable)
# Hint DNF that MRI is preferred interpreter.
Suggests: ruby
BuildArch: noarch

%description
Fedora /usr/bin/ruby stub to allow choosing Ruby runtime. Similarly to rbenv
or RVM, it allows non-privileged user to choose which is preferred Ruby
runtime for current task.

%prep
%setup -q


%build
# Nothing to do here.

%install
mkdir -p %{buildroot}%{_bindir}
cp -a ruby %{buildroot}%{_bindir}


%files
%doc README.md LICENSE
%{_bindir}/ruby


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 22 2015 Vít Ondruch <vondruch@redhat.com> - 1.1.1-4
- Use MRI by default.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 20 2014 Vít Ondruch <vondruch@redhat.com> - 1.1.1-1
- Update to rubypick 1.1.1.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Vít Ondruch <vondruch@redhat.com> - 1.1.0-1
- Update to rubypick 1.1.0.

* Wed Feb 06 2013 Vít Ondruch <vondruch@redhat.com> - 1.0.2-3
- Simplified source URL, since GH now provides tarball that better fits to
  RPM build.

* Mon Feb 04 2013 Vít Ondruch <vondruch@redhat.com> - 1.0.2-2
- Add dependency on some Ruby executable.

* Mon Feb 04 2013 Vít Ondruch <vondruch@redhat.com> - 1.0.2-2
- Initial package.
