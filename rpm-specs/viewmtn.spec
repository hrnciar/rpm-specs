%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global mtn_snapshot 1
%global mtn_rev 0030ad67c4daf3d38193f558c48474ddbcf19d1a
%global mtn_date 20100308

%if 0%{?mtn_snapshot}
%global mtn_short %(echo %{mtn_rev} | cut -c-8)
%endif

Name:           viewmtn
Version:        0.10
Release:        26%{?mtn_short:.%{mtn_date}mtn%{mtn_short}}%{?dist}
Summary:        Web interface for Monotone version control system
License:        GPLv2+
URL:            http://viewmtn.1erlei.de/
%if 0%{?mtn_snapshot}
# wget http://mtn-view.1erlei.de/revision/tar/%%{mtn_rev} -O- |
# bzip2 -c > %%{name}-%%{mtn_short}.tar.bz2
Source0:        %{name}-%{mtn_short}.tar.bz2
%else
Source0:        http://viewmtn.1erlei.de/downloads/%{name}-%{version}.tgz
%endif
Source1:        viewmtn.conf.httpd
Source2:        viewmtn.conf.py
BuildArch:      noarch
BuildRequires:  python2-devel
Requires:       python2-cheetah
# ensure the user 'apache' exists
Requires(pre):  httpd-filesystem
Requires:       monotone >= 0.46
Requires:       python2-mod_wsgi
Requires:       gnome-icon-theme
Requires:       shared-mime-info
Requires:       highlight
Requires:       graphviz

%global mydata  %{_datadir}/viewmtn
%global mypy    %{python_sitelib}/viewmtn
%global mygraph %{_localstatedir}/cache/viewmtn-graph


%description
ViewMTN is a web interface to the Monotone distributed version
control system.  It aims to provide a convenient and useful web
interface to Monotone.  If you've used interfaces to other version
control systems, ViewMTN will be immediately familiar.


%prep
%if 0%{?mtn_snapshot}
%setup -q -n %{mtn_rev}
%else
%setup -q
%endif

cat > __init__.py <<\EOF
from viewmtn import assemble_urls, web
urls, fvars = assemble_urls()
application = web.wsgifunc(web.webpyfunc(urls, fvars))
EOF


%build
sed -e s,__datadir__,%{_datadir}, \
    -e s,__python_sitelib__,%{python_sitelib}, %{SOURCE1} > viewmtn.conf
sed -e s,__datadir__,%{_datadir}, \
    -e s,__python_sitelib__,%{python_sitelib}, %{SOURCE2} > viewmtn.conf.py
sed -e s,/usr/bin,%{_bindir},g \
    -e '/^dbfile/s,= .*$,'"= '%{mydb}',"\
    -e '/^dynamic_uri_path/s,= .*$,'"= '/viewmtn/'," \
    -e '/^static_uri_path/s,= .*$,'"= '/viewmtn-static/'," \
    -e '/^templates_directory/s,= .*$,'"= '%{mydata}/templates/'," \
    -e '/viewmtn-graph/s|: .*$|'": '%{mygraph}/',|" \
    -e '/^running_under_apache2/s/$/ # not relevant to mod_wsgi setup/' \
    config.py.example > config.py

cat >> config.py <<\EOF

# Get the local configuration linked from %%{_sysconfdir}/.
from user_config import *
EOF


%install
install -d -m 755 %{buildroot}%{mypy}/fdo
install -d -m 755 %{buildroot}%{mypy}/web
install -d -m 755 %{buildroot}%{mydata}/templates
install -d -m 755 %{buildroot}%{mydata}/MochiKit
install -d -m 755 %{buildroot}%{mygraph}
install -Dp -m 0644 viewmtn.conf \
        %{buildroot}/%{_sysconfdir}/httpd/conf.d/viewmtn.conf
install -Dp -m 644 -t %{buildroot}%{mypy} *.py
install -Dp -m 644 -t %{buildroot}%{mypy}/fdo fdo/*.py
install -Dp -m 644 -t %{buildroot}%{mypy}/web web/*.py
install -Dp -m 644 -t %{buildroot}%{mydata}/templates templates/*.html
install -Dp -m 644 -t %{buildroot}%{mydata} \
        static/*.gif static/*.css static/*.js
install -Dp -m 644 -t %{buildroot}%{mydata}/MochiKit \
        static/MochiKit/*.js

install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -Dp -m 0644 viewmtn.conf.py \
        %{buildroot}%{_sysconfdir}/%{name}/conf.py

mypy_rel=`echo %{mypy} | sed 's,/[^/]*,../,g;s,/$,,'`
ln -snf $mypy_rel%{_sysconfdir}/%{name}/conf.py \
   %{buildroot}%{mypy}/user_config.py

# Pacify overeager rpmlint #! checks.
find %{buildroot}%{mypy} -type f -name '*.py' -print0 |
xargs -0 sed -i '1{/^#!/d;}'


%files
%doc README AUTHORS ChangeLog TODO INSTALL
%license LICENSE
%{mypy}
%{mydata}
%dir %attr(0755,apache,apache) %{mygraph}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/viewmtn.conf
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/conf.py*


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-26.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-25.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-24.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-23.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10-22.20100308mtn0030ad67
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-21.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-20.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-19.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov  9 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.10-18.20100308mtn0030ad67
- Justify Requires(pre) tag (#1319229).
- Mark LICENSE as %%license.

* Sun Nov 06 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.10-17.20100308mtn0030ad67
- Rebuilt against new highlight, spec cleanup

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-15.20100308mtn0030ad67
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-14.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-13.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-12.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-11.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-10.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-9.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-8.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7.20100308mtn0030ad67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug  6 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.10-6.20100308mtn0030ad67
- Update to latest head, to support monotone >= 0.46.
- Minor specfile updates.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.10-2
- Rebuild for Python 2.6

* Sun Mar 23 2008 Roland McGrath <roland@redhat.com> - 0.10-1
- New package.  Thanks to Thomas Moschny for packaging assistance.
