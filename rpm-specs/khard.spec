%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           khard
Version:        0.11.4
Release:        11%{?dist}
Summary:        An address book for the Linux console

License:        GPLv3
URL:            https://github.com/scheibler/%{name}
Source0:        https://github.com/scheibler/%{name}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pypandoc
Requires:       python3-atomicwrites
Requires:       python3-configobj
Requires:       python3-PyYAML
Requires:       python3-vobject

%description
Khard is an address book for the Linux console. It creates, reads, modifies and
removes carddav address book entries at your local machine.


%prep
%setup -q -n %{name}-%{version}


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
for lib in %{buildroot}%{python_sitelib}/khard/*.py; do
    sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
    touch -r $lib $lib.new &&
    mv $lib.new $lib
done
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
install -p -m 0644 misc/zsh/_khard %{buildroot}%{_datadir}/zsh/site-functions/_khard


%files
%doc AUTHORS CHANGES README.md
%doc misc/khard/khard.conf.example
%license LICENSE
%{_bindir}/khard
%{python3_sitelib}/*
%{_datadir}/zsh/site-functions/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.4-11
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.4-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.4-8
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11.4-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Sebastian Dyroff <sdyroff@fedoraproject.org> - 0.11.4-1
- update to 0.11.4 fixing #1473961

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.11.3-2
- Rebuild for Python 3.6

* Sat Oct 08 2016 Ben Boeckel <mathstuf@gmail.com> - 0.11.3-1
- update to 0.11.3

* Tue Aug 02 2016 Ben Boeckel <mathstuf@gmail.com> - 0.11.1-2
- add BR on python3-pypandoc
- remove utf8-readme patch

* Tue Aug 02 2016 Ben Boeckel <mathstuf@gmail.com> - 0.11.1-1
- update to 0.11.1

* Sat Jul 23 2016 Ben Boeckel <mathstuf@gmail.com> - 0.11.0-1
- update to 0.11.0
- remove davcontroller (masked upstream due to python3 compat issues)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Apr 23 2016 Ben Boeckel <mathstuf@gmail.com> - - 0.9.0-1
- update to 0.9.0

* Mon Apr 04 2016 Ben Boeckel <mathstuf@gmail.com> - 0.8.1-1
- update to 0.8.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 25 2015 Ben Boeckel <mathstuf@gmail.com> - 0.6.3-1
- update to 0.6.3

* Tue Oct 13 2015 Ben Boeckel <mathstuf@gmail.com> - 0.6.2-1
- update to 0.6.2
- ship zsh completion file

* Sat Jul 25 2015 Ben Boeckel <mathstuf@gmail.com> - 0.4.1-1
- update to 0.4.1
- remove shebang lines

* Tue Mar 03 2015 Ben Boeckel <mathstuf@gmail.com> - 0.2.1-2
- use python2-devel in BR
- chmod +x davcontroller.py
- remove twinkle plugin (twinkle isn't in Fedora)

* Tue Mar 03 2015 Ben Boeckel <mathstuf@gmail.com> - 0.2.1-1
- initial package
